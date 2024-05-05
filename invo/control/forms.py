from django import forms
from .models import Item,Expense


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','price','client')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount', 'description',)