from django.db import models
from django.utils import timezone
from .item_model import Item
from .customer_model import Customer


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        item_names = [item.name for item in self.items.all()]
        item_names_str = ", ".join(item_names)
        return f"Purchase: {item_names_str}"
