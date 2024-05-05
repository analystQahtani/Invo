from django.urls import path
from . import views
#from django.conf.urls import url

app_name = 'control'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('sellers/', views.sellers, name='sellers'),
    path('expenses/', views.expenses, name='expenses'),
]