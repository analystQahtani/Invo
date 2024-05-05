from django.urls import path
from . import views
#from django.conf.urls import url
from . import views
#from invo import control

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard ,name='dashboard'),
    path('invoice/', views.invoice, name='invoice'),
    path('customers/', views.customers, name='customers'),
    path('items/', views.items, name='items'),
    path('sellers/', views.sellers, name='sellers'),
    path('logout/', views.logout, name='logout'),
]