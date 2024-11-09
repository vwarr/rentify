from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserProfile


# Create your models here.
class RentalItem(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    renter_first_name = models.CharField(max_length=50)
    renter_last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.item_name
    