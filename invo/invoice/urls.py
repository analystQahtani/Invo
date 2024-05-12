from django.urls import path
from . import views
#from django.conf.urls import url

app_name = 'invoice'

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('create/', views.InvoiceCreate.as_view(), name="invoice-create"),
    #path('<int:pk>/delete/',views.edit_invoice,name='edit_invoice'),
    path('<int:pk>/delete/',views.delete_invoice,name='delete_invoice'),
    path('<int:pk>/view/',views.GenerateInvoice.as_view(),name='view_invoice'),


    path('customers/', views.customers, name='customers'),
    path('customers/<int:pk>/edit/',views.edit_customer,name='edit_customer'),
    #path('customers/<int:pk>/update/',views.update_customer,name='update_customer'),
    path('customers/<int:pk>/delete/',views.delete_customer,name='delete_customer'),
]