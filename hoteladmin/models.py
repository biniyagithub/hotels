from django.db import models

# Create your models here.
class Hotel(models.Model):
    hname = models.CharField(max_length=100)
    haddress = models.CharField(max_length=100)
    himage = models.ImageField(upload_to='data',default='null.jpg')
    hprice = models.IntegerField()
    hdescription = models.CharField(max_length=100)
    hstate = models.CharField(max_length=100)
    hcity = models.CharField(max_length=100)
    hpin = models.IntegerField()
    hemail = models.EmailField()
    hpassword = models.CharField(max_length=100)


    
