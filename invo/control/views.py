from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Client
from .forms import ExpenseForm, ItemForm
from .models import Expense, Item
from django.views.generic import ListView


################################################################
@login_required
def items(request):
    items = Item.objects.all()
        
    print(request.tenant)
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            #expense.created_by = request.user

            #expense.client = Client.objects.get(user=request.user)
            item.save()

            return redirect('.')
    
    else:
        form = ItemForm()
        #form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'control/items.html',{
        "form": form, "items" : items
    })

#def expenses(request):
#    return render(request, 'control/expenses.html')

def sellers(request):
    return render(request, 'control/sellers.html')


@login_required
def expenses(request):
    
    expenses = Expense.objects.all()

    print(request.tenant)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            #expense.created_by = request.user

            #expense.client = Client.objects.get(user=request.user)
            expense.save()

            return redirect('.')
    
    else:
        form = ExpenseForm()
        #form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'control/expenses.html',{
        "form": form, "expenses" : expenses
    })

@login_required
def edit_expense(request, pk):  
    expense = Expense.objects.get(pk=pk)  
    return render(request,'control/edit_expense.html', {'expense':expense})  

@login_required
def update_expense(request, pk):  
    expense = Expense.objects.get(pk=pk)  
    form = ExpenseForm(request.POST, instance = expense)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'control/edit_expense.html', {'expense': expense})  



@login_required
def delete_expense(request,pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()

    redirect('/dashboard/')

    return render(request, 'dashboard/dashboard.html')

@login_required
def edit_item(request,pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance = item )

        if form.is_valid():
            form.save()

            return redirect('.')
    else:
        form = ItemForm(instance = item)


    return render(request, 'control/items.html',{
        "form": form,
        "title": "edit item",
    })

@login_required
def delete_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()

    redirect('/dashboard/')

    return render(request, 'dashboard/dashboard.html')

@login_required
def add_seller(request):
    #sellers 
    pass