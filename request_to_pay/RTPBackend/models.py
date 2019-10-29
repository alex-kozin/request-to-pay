from django.db import models


class Invoice(models.Model):
    STATUS_CHOICES = [("A", "Active"), ("P", "Paid"), ("D", "Delivered")]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    customer = models.ForeignKey("userapi.UserProfile",related_name="invoices_to_pay" , on_delete=models.CASCADE)
    driver = models.ForeignKey("userapi.UserProfile",related_name="invoices_to_check" , on_delete=models.CASCADE)

    def _calculate_price(self):
        "Returns the price of the invoice"
        return sum(int(order.price) for order in self.orders.all())
    price = property(_calculate_price)


class Order(models.Model):
    invoice = models.ForeignKey("Invoice", related_name="orders", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def _calculate_price(self):
        "Returns the price of the order"
        return self.quantity * getattr(self.item, "price")
    price = property(_calculate_price)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12)
