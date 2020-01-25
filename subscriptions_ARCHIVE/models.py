from django.db import models
from django.conf import settings

from datetime import date

class Subscription(models.Model):
    """ Data model for a user's subscription """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    expiry_date = models.DateField()

    def __str__(self):
        return "Subscription for user {}".format(self.pk)

    def is_active(self):
        """ Return true if subscription is not expired """
        if self.expiry_date >= date.today():
            return True
        else:
            return False

class Payment(models.Model):
    """ Data model for a record of payment """
    user_subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    stripe_ref = models.CharField(max_length=30, null=True)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return "Payment for subscription {}".format(self.user_subscription.pk)