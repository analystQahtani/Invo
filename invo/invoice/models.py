'''from django.db import models
from django.contrib.auth.models import User
from accounts.models import Client
from management.models import Item

class Invoice(models.Model):

    def increment_invoice_number():
        last_invoice = Invoice.objects.all().order_by('id').last()
        if not last_invoice:
            return 'INV0001'
        invoice_no = last_invoice.invoiceNumber
        invoice_int = int(invoice_no.split('INV')[-1])
        width = 4
        new_invoice_int = invoice_int + 1
        formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
        new_invoice_no = 'INV' + str(formatted)
        return new_invoice_no

    invoiceNumber = models.CharField(max_length = 500, default = increment_invoice_number, null = True, blank = True)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = "seller")
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = "customer")
    item = models.ManyToManyField(Item)
    quantity = models.IntegerField(null = True)
    amount = models.FloatField(null = True)
    discount = models.FloatField(null = True)
    tax = models.FloatField(null = True)
    total = models.FloatField(null = True)

    def __str__(self):
        return f"{self.name}"

'''