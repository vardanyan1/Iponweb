from django.db import models
from ...tools.image_preproc_tools import handle_uploaded_file


class ItemsCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=handle_uploaded_file)

    def __str__(self):
        return self.name
