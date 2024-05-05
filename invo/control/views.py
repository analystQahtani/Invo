from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Client
from .forms import ExpenseForm, ItemForm

################################################################
def items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            #expense.created_by = request.user

            #item.client = Client.objects.get(user=request.user)
            #item.save()

            return redirect('/dashboard/')
    
    else:
        form = ItemForm()
    return render(request, 'control/items.html',{
        "form": form,
    })

#def expenses(request):
#    return render(request, 'control/expenses.html')

def sellers(request):
    return render(request, 'control/sellers.html')


@login_required
def expenses(request):
    print(request.tenant)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            #expense.created_by = request.user

            expense.client = Client.objects.get(user=request.user)
            expense.save()

            return redirect('/dashboard/')
    
    else:
        form = ExpenseForm()
        #form.fields['category'].queryset = Category.objects.filter(created_by = request.user)

    return render(request, 'control/expenses.html',{
        "form": form,
    })
