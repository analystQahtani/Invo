from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import Client
#from dashboard.models import Account

def logout(request):
  auth.logout(request)
  return render(request,'accounts/signin.html')

def dashboard(request):
  #user = Client.objects.filter(user=request.user)
  return render(request,'dashboard/dashboard.html')

def items(request):
  return render(request, 'control/items.html')

def invoice(request):
  return render(request, 'invoice/invoices.html')

def customers(request):
  return render(request, 'invoice/customers.html')

def sellers(request):
  return render(request, 'control/sellers.html')

