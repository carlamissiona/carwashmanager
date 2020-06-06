from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100,null=True)
    pub_date = models.DateTimeField('publish date', auto_now_add=True)

class StockItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=40, null=True)
    qty = models.PositiveSmallIntegerField(null=True)
    pub_date = models.DateTimeField('publish date', auto_now_add=True)

class Sales(models.Model):
	
    car_qty = models.PositiveSmallIntegerField()
    sale_amount  = models.PositiveIntegerField()
    service  = models.CharField(max_length=100,default='Wax & Wash')
    staff  = models.CharField(max_length=100,default='Junior')
    pub_date = models.DateTimeField('date of sale', auto_now_add=True)

