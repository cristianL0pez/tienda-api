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
