from django.db import models
from django.conf import settings

class Payment(models.Model):
    """ Data model for a record of payment """
    payment_date = models.DateTimeField(auto_now_add=True)
    stripe_ref = models.CharField(max_length=30, null=True)
    amount = models.IntegerField(null=True)

class Subscription(models.Model):
    """ Data model for a user's subscription """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    last_payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)
    expiry_date = models.DateField()