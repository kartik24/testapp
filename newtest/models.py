from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)
    price       = models.CharField(max_length=200, null=True, blank=True)
    image   = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = u'Product'

class Contact(models.Model):
    Name    = models.CharField(max_length=200, null=True, blank=True)
    Email   = models.EmailField(max_length=200, null=True, blank=True)
    Message = models.TextField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = u'Contact'

class Register(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    Email = models.EmailField(max_length=200, null=False, blank=False)
    Password = models.CharField(max_length=20, null=False, blank=False)
    Number = models.CharField(max_length=10, null=False, blank=False)
    City = models.CharField(max_length=30, null=False, blank=False)
    Country = models.CharField(max_length=30, null=False, blank=False)
    class Meta:
        db_table = u'Register'



