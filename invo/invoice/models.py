from django.db import models
from django.contrib.auth.models import User
from accounts.models import Client
from control.models import Item


class Customer(models.Model):
    name = models.CharField(max_length = 100)
    number = models.CharField(max_length = 10) 
    email = models.EmailField()


    def __str__(self):
        return f"{self.name}"



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
    date = models.DateTimeField(auto_now_add=True)
    #seller = models.ForeignKey(User, on_delete = models.CASECADE, null = True, related_name = "seller")
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, null = True, related_name = "customer")
    #item = models.ForeignKey(Item, on_delete = models.CASCADE, null = True, related_name = "item")
    #quantity = models.IntegerField(null = True)
    #amount = models.FloatField(null = True)
    #discount = models.FloatField(null = True)
    #tax = models.FloatField(null = True)
    #total = models.FloatField(null = True)

    @property
    def total_order(self):
        invoice_items = InvoiceItem.objects.filter(invoice_id=self.id)
        sum = 0
        for invoice_item in invoice_items:
            sum = sum + invoice_item.price
        return sum


    @property
    def total_qty(self):
        invoice_items = InvoiceItem.objects.filter(invoice_id=self.id)
        total_qty = 0
        for invoice_item in invoice_items:
            total_qty = (invoice_item.qty + total_qty)
        return total_qty


    #def __str__(self):
    #    return self.customer.first_name.title() +" "+self.customer.last_name.title()
    
    def __str__(self):
        return f"{self.name}"


class InvoiceItem(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    qty = models.IntegerField(default=0)
    #price = models.FloatField()
    #amount = models.FloatField()

    @property
    def price(self):
         return self.qty * self.item.price


    def __str__(self):
        return self.item.name +" "+ str(self.qty)
    
    #def __str__(self):
    #    return str(self.invoice)

