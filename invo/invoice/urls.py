from django.urls import path
from . import views
#from django.conf.urls import url

app_name = 'invoice'

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('customers/', views.customers, name='customers'),
]