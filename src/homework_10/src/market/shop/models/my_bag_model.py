from django.db import models
from .customer_model import Customer
from .item_model import Item


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        item_names = [item.name for item in self.items.all()]
        item_names_str = ", ".join(item_names)
        return f"Bag with: {item_names_str}"
