from django.db import models

#modelo cliente
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail= models.EmailField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    address= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    image= models.ImageField(upload_to='api/images', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

   

#modelo producto
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='api/images', null=True, blank=True)
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#modelo proveedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='api/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
