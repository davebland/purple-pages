from django.test import TestCase
from django.http import JsonResponse, HttpResponseBadRequest

from datetime import date, timedelta
import json
from unittest import skipIf
import os

from .models import PPUser, Payment
from .forms import PPUserCreationForm
from .stripe import stripe_payment_intent, stripe_confirm_payment

class TestAccountsModels(TestCase):
    """ Tests for accounts models """

    def test_ppuser_and_subscription_status(self):
        """ Create user and test subscription status """        
        user = PPUser()
        user.save()
        self.assertEqual(user.subscription_status(), 0)
        user.subscription_expiry = date.today()
        user.save()
        self.assertEqual(user.subscription_status(), 1)
        user.subscription_expiry = date.today() - timedelta(days=1)
        user.save()
        self.assertEqual(user.subscription_status(), 2)

    def test_payment_object(self):
        """ Create a user and payment object then check attributes """
        user = PPUser()
        user.save()
        payment = Payment(amount=500, user=user)
        payment.save()
        self.assertEqual(payment.amount, 500)
        self.assertEqual(payment.user, PPUser.objects.get(pk=1))
        self.assertEqual(str(payment), "Payment of £5.00 for ")

class TestAccountViews(TestCase):
    """ Tests for account views """

    def test_account_view(self):
        """ Test My Account view returns correct template and user_stats object """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Get page and test
        page = self.client.get("/account/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'my_account.html')
        self.assertIsInstance(page.context['user_stats'], dict)

    def test_my_ads_view(self):
        """ Test My Ads view returns correct template """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Get page and test
        page = self.client.get("/account/my_ads/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'my_ads.html')

    def test_registration_view(self):
        """ Test Registration view returns correct template """
        page = self.client.get("/account/registration/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')        

    def test_subscription_view(self):
        """ Test subscription view returns correct template """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Get page and test
        page = self.client.get("/account/subscription/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'my_subscription.html')

class TestAccountForms(TestCase):
    """ Tests for account forms """    

    def test_PPUserCreationForm(self):
        """ Test creating and saving a new user form """
        form = PPUserCreationForm({'username':'testuser', 'password1':'test password', 'password2':'test password'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.save(),PPUser.objects.get(pk=1))

class TestStripe(TestCase):
    """ Test for PP Stripe """

    @skipIf(os.getenv('STRIPE_SECRET_KEY')==None,"Stripe Not Setup")
    def test_create_subscription_view(self):
        """ Test Stripe Create Subscription view returns a valid JSON response """                
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # test create subscription view
        page = self.client.post("/account/create_payment/", {'subscription-period':100}, follow=True)
        self.assertEqual(page.status_code, 200)    

    @skipIf(os.getenv('STRIPE_SECRET_KEY')==None,"Stripe Not Setup")
    def test_stripe_webhook_view(self):
        """ Test Stripe webhook handler returns 400 when not presented with stripe payment intent """        
        endpoint = self.client.post("/account/confirm_payment/", {}, follow=True)
        self.assertEqual(endpoint.status_code, 400)

#     def test_stripe_payment_intent(self):
#         """ Test create payment intent """        
#         intent = stripe_payment_intent({'payment_amount':100,'period':100,'pp_username':1})
#         self.assertIsInstance(intent, JsonResponse)

#     def test_stripe_webhook(self):
#         """ Test handling webhook data (stripe_confirm_payment) """
#         webhook = stripe_confirm_payment({})
#         self.assertIsInstance(webhook, HttpResponseBadRequest) 