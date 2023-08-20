from django.db import models

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

    def __str__(self):
        return f"{self.name} - {self.quantity}"
