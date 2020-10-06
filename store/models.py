from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Home (models.Model):
    name = models.CharField(max_length=200,null=False)
    image = models.ImageField(null=True, blank=False)

class Product(models.Model):
    price = models.FloatField()
    description = models.CharField(max_length=1000,null=True)

    name = models.CharField(max_length=1000,null=False)
    image = models.ImageField(null=True, blank=False)

	#name = models.ForeignKey(Home, null=True, on_delete= models.SET_NULL)
	#image = models.ForeignKey(Home, related_name='related_photo',null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ShippingAddress(models.Model):

	
    customer_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=10, null=False)
    payment = models.CharField(max_length=100, null=False,)

    name = models.CharField(max_length=1000,null=True)
    price = models.CharField(max_length=1000,null=True)
    image = models.ImageField(null=True, blank=True)

	#name = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	#price = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL))
	#image = models.ForeignKey(Product, related_name='related_photo',null=True)

    def __str__(self):
        return self.address



