from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='stores')

    def __str__(self):
        return f"Store name: {self.name}"

class ItemsCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='items')

    def __str__(self):
        return f"Item name: {self.name}"
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='Customer')
    registered_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"User: {self.user.username}, registered: {self.registered_at}"

