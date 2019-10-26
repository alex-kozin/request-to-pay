from django.db import models

class Invoice(models.Model):
    STATUS_CHOICES = [("A", "Active"), ("P", "Paid"), ("D", "Delivered")]
    price = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    customer_id = models.ForeignKey("UserProfile", on_delete=models.CASCADE)


class Order(models.Model):
    invoice_id = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    ##ALTERNTAIVELY: item_type
    item_id = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    driver_id = models.ForeignKey("UserProfile", on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12)


class UserProfile(models.Model):
    USER_CHOICES = [("S", "Suppliers"), ("C", "Customer"), ("D", "Driver")]
    name = models.CharField
    address = models.TextField(blank=True)
    user_type = models.CharField(choices=USER_CHOICES, max_length=1)
    status = models.BooleanField()