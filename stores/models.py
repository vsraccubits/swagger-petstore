from django.db import models
from django.utils.translation import gettext_lazy as _

from pets.models import Pet


class Address(models.Model):
    """
    Model to store address details.
    """

    street = models.CharField(max_length=100, verbose_name=_("Street"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    zip = models.CharField(max_length=100, verbose_name=_("Zip"))

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "%s - %s" % (self.name, self.zip)


class Customer(models.Model):
    """
    Model to store customer details.
    """

    username = models.CharField(max_length=100, verbose_name=_("Customer Username"))
    addresses = models.ManyToManyField(Address, verbose_name=_("Customer Addresses"))

    def __str__(self):
        return self.username


class Order(models.Model):
    """
    Model to store order details.
    """

    class OrderStatuses(models.TextChoices):
        PLACED = "placed", _("Placed")
        APPROVED = "approved", _("Approved")
        DELIVERED = "delivered", _("Delivered")

    pet = models.ForeignKey(Pet, on_delete=models.PROTECT, verbose_name=_("Order Pet"))
    quantity = models.PositiveSmallIntegerField(verbose_name=_("Order Quantity"))
    ship_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Order Date Time")
    )
    status = models.CharField(
        max_length=30,
        choices=OrderStatuses.choices,
        default=OrderStatuses.PLACED,
        verbose_name=_("Order Status"),
    )
    complete = models.BooleanField(default=False, verbose_name=_("Order Complete"))

    def __str__(self):
        return "Order - %s" % (self.ship_date)
