from django.db import models
from django.contrib.auth.models import User
admin = 'RushX'

# Create your models here.
class Product(models.Model):
    ID_of_the_Product = models.AutoField
    Product_Name = models.CharField(max_length=50)
    Cateogary = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    Description = models.TextField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='icommerce/images', blank=True, null=True)
    linkToDownload = models.CharField(max_length=500, default='')
    
    # User-generated product fields
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.Product_Name

class Order(models.Model):
    country = models.CharField(max_length=20, default='')
    amount = models.CharField(max_length=20)
    itemsJson = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstName

class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fname} tried to contact {admin}'