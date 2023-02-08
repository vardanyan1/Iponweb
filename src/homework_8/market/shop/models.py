from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib
import os

def hash_file_name(filename):
    hash_object = hashlib.sha256(filename.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def handle_uploaded_file(instance, filename):
    sub_folder = instance.__class__.__name__.lower()
    extension = os.path.splitext(filename)[1]
    hashed_filename = hash_file_name(filename) + extension
    return os.path.join(sub_folder, hashed_filename)


# Create your models here.
class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=handle_uploaded_file)

    def __str__(self):
        return self.name

class ItemsCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=handle_uploaded_file)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=handle_uploaded_file)
    registered_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username

class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=handle_uploaded_file)
    registered_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Store(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=handle_uploaded_file)
    category = models.ForeignKey(ItemsCategory, on_delete=models.SET_DEFAULT, default="Not set")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    info = models.TextField(max_length=600)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# MyBug
# Fields: customer (ForeignKey to Customer), items (ManyToMany to Item), total_price
# Purchase
# Fields: items (ManyToMany to Item), buy_time, customer (ForeignKey to Customer),
# total_price.
