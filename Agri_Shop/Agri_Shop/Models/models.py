from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table_comment = "Farmer"


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table_comment = "Client"


class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity_in_stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table_comment = "Product"
    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateOrder = models.DateField()
    TypeOfPaymant = models.CharField(max_length=255)
    class Meta:
        db_table_comment = "Order"
        

class OrderDetails(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField(default=0)
    class Meta:
        db_table_comment = "OrderDetails"