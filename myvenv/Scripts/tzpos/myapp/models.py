from django.db import models

# Create your models here.
class Supplier(models.Model):
    sup_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    
    def __str__(self):
        return self.sup_name
