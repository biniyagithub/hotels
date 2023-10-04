from django.db import models

# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=100)
    caddress = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to='data',default='null.jpg')
    cplace = models.CharField(max_length=100)
    cemail = models.EmailField()
    cpassword = models.CharField(max_length=100)
    checkindate = models.DateField()
    checkoutdate = models.DateField()
    rooms = models.IntegerField()


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)