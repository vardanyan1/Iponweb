from django.db import models
from .store_owner_model import StoreOwner
from .store_category_model import StoreCategory


class Store(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
