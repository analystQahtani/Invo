from django.urls import path
from . import views
#from django.conf.urls import url

app_name = 'control'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/<int:pk>/edit/',views.edit_item,name='edit_item'),
    #path('items/<int:pk>/update/',views.update_item,name='update_item'),
    path('items/<int:pk>/delete/',views.delete_item,name='delete_item'),

    path('sellers/', views.sellers, name='sellers'),

    path('expenses/', views.expenses, name='expenses'),
    path('expenses/<int:pk>/edit/',views.edit_expense,name='edit_expense'),
    path('expenses/<int:pk>/update/',views.update_expense,name='update_expense'),
    path('expenses/<int:pk>/delete/',views.delete_expense,name='delete_expense'),


]