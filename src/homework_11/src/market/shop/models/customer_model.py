from django.db import models
from ...tools.image_preproc_tools import handle_uploaded_file
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=handle_uploaded_file, blank=True, null=True)
    registered_at = models.DateField(default=timezone.now().date())

    def __str__(self):
        return self.user.username
