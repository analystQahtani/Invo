from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

class Client(TenantMixin):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "user", null= True)
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return f"{self.name}"

class Domain(DomainMixin):
    pass

'''class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client")
'''