from django.db import models
from accounts.models import Client

class Item(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField(null = True)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)

class Expense(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    amount = models.FloatField(null = True)
    description = models.TextField(blank=True, null= True)
