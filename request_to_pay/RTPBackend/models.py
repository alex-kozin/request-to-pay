from django.db import models

class Invoice(models.Model):
    STATUS_CHOICES = [("A", "Active"), ("P", "Paid"), ("D", "Delivered")]
    price = models.DecimalField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    customer_id = models.ForeignKey("UserProfile")


class Order(models.Model):
    invoice_id = models.ForeignKey("Invoice")
    ##ALTERNTAIVELY: item_type
    item_id = models.ForeignKey("Item")
    quantity = models.IntegerField()
    price = models.DecimalField()
    driver_id = models.ForeignKey("UserProfile")


class Item(models.Model):
    name = models.CharField()
    price = models.DecimalField()


class UserProfile(models.Model):
    USER_CHOICES = [("S", "Suppliers"), ("C", "Customer"), ("D", "Driver")]
    name = models.CharField
    address =  models.TextField(blank=True)
    user_type = models.CharField(choices=USER_CHOICES, max_length=1)
    status = models.BooleanField()