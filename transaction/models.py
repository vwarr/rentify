from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import UserProfile

class UserPayment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    payment_success = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)


@receiver(post_save, sender=UserProfile)
def create_payment(sender, instance, created, **kwargs):
    if created:
        UserPayment.objects.create(user=instance)



