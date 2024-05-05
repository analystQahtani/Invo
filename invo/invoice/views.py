from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_tenants.utils import tenant_context
from accounts.models import Client
#from.models import Invoice, Item

#@login_required
def invoice(request):
    
    return render(request, 'invoice/invoices.html')

'''
#@login_required
def new_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        User.objects.create_user(first_name = name, email = email, is_superuser = False, is_staff = False)


    return render(request, 'invoice/customers.html')
'''
#@login_required
def customers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = "cust" + str(User.objects.filter())

        tenant = Client.objects.filter(schema_name = request.tenant)
        with tenant_context(tenant):
            User.objects.create_user(username = username, first_name = name, email = email, is_superuser = False, is_staff = False)
    
    customers = User.objects.filter(is_staff = False)

    return render(request, 'invoice/customers.html')#{'customer' : customers}