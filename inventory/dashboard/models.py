from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
    ("Stationary", "Stationary"),
    ("Electronics", "Electronics"),
    ("Food", "Food"),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=20, null=True)
    quantity = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self):
        return f"{self.product} - ordered by {self.staff.username}"
