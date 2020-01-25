from django.test import TestCase

from datetime import date, timedelta

from accounts.models import PPUser, Payment

class TestAccountsModels(TestCase):
    """ Tests for accounts models """

    def test_ppuser_subscription_status(self):
        """ Create a user and test subscription status """
        user = PPUser()
        user.save()
        self.assertEqual(user.subscription_status(), 'No Subscription')
        user.subscription_expiry = date.today()
        user.save()
        self.assertEqual(user.subscription_status(), 'Active')
        user.subscription_expiry = date.today() - timedelta(days=1)
        user.save()
        self.assertEqual(user.subscription_status(), 'Expired')

    def test_payment_object(self):
        """ Create a user and payment object then check attributes """
        user = PPUser()
        user.save()
        payment = Payment(amount=5, user=user)
        payment.save()
        self.assertEqual(payment.amount, 5)
        self.assertEqual(payment.user, PPUser.objects.get(pk=1))
        self.assertEqual(str(payment), "Payment of £5 for user 1")