from .models import Customer, Invoice, InvoiceItem
from django import forms
from django.forms import formset_factory

from django.forms import inlineformset_factory



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','number', 'email',)


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ('item', 'qty', )


InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm)
