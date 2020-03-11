from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date

from boards.models import Board

class PPUser(AbstractUser):
    """ Data model for a Purple Pages User (extends django User) """

    favourite_board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True)
    subscription_expiry = models.DateField(null=True, blank=True)

    def subscription_status(self):
        """ Return subscription status as integer (0 None, 1 Active, 2 Expired) """
        if self.subscription_expiry:
            if self.subscription_expiry >= date.today():
                return 1
            else:
                return 2
        else:
            return 0

class Payment(models.Model):
    """ Data model for a record of payment """
    
    payment_date = models.DateTimeField(auto_now_add=True)
    stripe_ref = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField()

    user = models.ForeignKey(PPUser, on_delete=models.PROTECT)

    def __str__(self):
        return "Payment of £{:.2f} for {}".format(self.amount/100, self.user.username)