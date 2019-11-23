from django.db import models


class Invoice(models.Model):
    """
    An invoice from Coke to Small Business Owner.

    Fields
    ----------
    status: CharField
        the current status of this invoice, can be:
        "A" - Active, "P" - Paid, "D" - Delivered

    customer: UserProfile
        the customer that has to pay this invoice

    driver: UserProfile
        the driver that has to deliver goods mentioned in the invoice

    Related Fields
    --------------
    orders: List[Order] (Related field)
        the orders related to this invoice

    Properties
    ----------
    price: Decimal
        the price customer has to pay for the goods mentioned on this invoice

    === Representation Invariants ===
    -   status: "A" | "P" | "D"
    -   len(status) == 1
    -   customer.usertype == 'C'
    -   driver.usertype == 'D'
    -   price is the sum of prices for all orders on the invoice
    """
    STATUS_CHOICES = [("A", "Active"), ("P", "Paid"), ("D", "Delivered")]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)

    customer = models.ForeignKey("userapi.UserProfile",
                                 related_name="invoices_to_pay",
                                 on_delete=models.CASCADE,
                                 limit_choices_to={'user_type': 'C'}
                                 )

    driver = models.ForeignKey("userapi.UserProfile",
                               related_name="invoices_to_check",
                               on_delete=models.CASCADE,
                               limit_choices_to={'user_type': 'D'}
                               )

    def _calculate_price(self):
        "Returns the price of the invoice"
        return sum(int(order.price) for order in self.orders.all())
    price = property(_calculate_price)

    def __str__(self):
        return f"{self.id}"


class Order(models.Model):
    """
    An order for some item. Each order represents how many items of the same
    item type were ordered.

    Fields
    ----------
    invoice: Invoice
        the invoice this order belongs to

    item: Item
        the type of the item ordered

    quantity: IntegerField
        the number of items ordered

    Properties
    ----------
    price: Decimal
        the price of the order

    === Representation Invariants ===
    -   quantity > 0
    -   price == quantity * item.price
    """
    invoice = models.ForeignKey("Invoice", related_name="orders",
                                on_delete=models.CASCADE)

    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def _calculate_price(self):
        "Returns the price of the order"
        return self.quantity * getattr(self.item, "price")
    price = property(_calculate_price)

    def __str__(self):
        return f"{self.quantity} x {self.item} @ ${self.price}"


class Item(models.Model):
    """
    An item available for purchase.

    Fields
    ----------
    name: CharField
        the name of the item

    price: DecimalField
        the price of the item

    === Representation Invariants ===
    -   len(name) >= 50
    -   0 < price <= 999999999999.99
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name
