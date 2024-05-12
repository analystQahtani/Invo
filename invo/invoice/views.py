from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django_tenants.utils import tenant_context
from accounts.models import Client
from .models import Customer, Invoice, InvoiceItem
from .forms import CustomerForm, InvoiceForm, InvoiceItemFormset
from control.models import Item
import pdfkit
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View

#formset
from django.forms import inlineformset_factory
#atomic
from django.db import transaction

@login_required
def invoice(request):
    invoices = Invoice.objects.all()
    customers = Customer.objects.filter()
    items = Item.objects.all()
    
    return render(request, 'invoice/invoices.html', {"invoices" : invoices, "customers" : customers,"items" : items})



@method_decorator(login_required, name='dispatch')
class InvoiceCreate(CreateView):
    model = Invoice
    fields = ['customer']
    template_name = 'invoice/invoice_create.html'
    success_url = reverse_lazy('invoice:invoice')

    def get_context_data(self, **kwargs):
        data = super(InvoiceCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = InvoiceItemFormset(self.request.POST)
        else:
            data['items'] = InvoiceItemFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()

        return super(InvoiceCreate, self).form_valid(form)

def invoice_update(request, invoice_id):

    invoice = Invoice.objects.get(id=invoice_id)
    form = InvoiceForm(request.POST, instance=invoice)
    ItemFormset = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceForm, extra=1)

    if request.method == 'POST':

        formset = ItemFormset(request.POST, instance=Invoice)

        if formset.is_valid():
            form.save()
            formset.save()
            from django.contrib import messages
            messages.success(request, 'Order successfully updated')
    else:

        form = InvoiceForm(instance=invoice)
        formset = ItemFormset(instance=invoice)

    return render(request, 'invoice/invoice_update.html', {'form':form, 'formset' : formset})


@login_required
def delete_invoice(request,pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.delete()

    redirect('/dashboard/')

    return render(request, 'invoice/invoice.html')

@login_required
def customers(request):
    customers = Customer.objects.all()
        
    print(request.tenant)
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            #expense.created_by = request.user

            #expense.client = Client.objects.get(user=request.user)
            customer.save()

            return redirect('.')
    
    else:
        form = CustomerForm()
        #form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'invoice/customers.html',{
        "form": form, "customers" : customers
    })

@login_required
def edit_customer(request, pk):  
    customer = Customer.objects.get(pk=pk)  
    return render(request,'invoice/customers.html', {'customer':customer})  

@login_required
def update_customer(request, pk):  
    customer = Customer.objects.get(pk=pk)  
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'invoice/customers.html', {'customer': customer})  



@login_required
def delete_customer(request,pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()

    redirect('/dashboard/')

    return render(request, 'invoice/customers.html')

##########################
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
#from xhtml2pdf import pisa
import os
import xhtml2pdf.pisa as pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenerateInvoice(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id = pk) 
        except:
            return HttpResponse("505 Not Found")
        data = {
            'invoice_id': invoice.pk,
            'transaction_id': invoice.invoiceNumber,
            'user_email': invoice.customer.email,
            'date': str(invoice.date),
            'name': invoice.customer.name,
            'order': invoice,
            'amount': invoice.total_order,
        }
        pdf = render_to_pdf('invoice/invoicePDF.html', data)
        #return HttpResponse(pdf, content_type='application/pdf')
        # force download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(data['transaction_id'])
            content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
