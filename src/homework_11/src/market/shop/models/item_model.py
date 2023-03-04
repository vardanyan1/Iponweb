from django.db import models
from ...tools.image_preproc_tools import handle_uploaded_file
from .items_category_model import ItemsCategory
from .store_model import Store


class Item(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=handle_uploaded_file, blank=True, null=True)
    category = models.ForeignKey(ItemsCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    info = models.TextField(max_length=600)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

