from django.db import models


class Invoice(models.Model):
    STATUS_CHOICES = [("A", "Active"), ("P", "Paid"), ("D", "Delivered")]
    price = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    customer = models.ForeignKey("userapi.UserProfile", on_delete=models.CASCADE)


class Order(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    driver = models.ForeignKey("userapi.UserProfile", on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12)
