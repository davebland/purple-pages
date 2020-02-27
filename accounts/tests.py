from django.test import TestCase

from datetime import date, timedelta

from .models import PPUser, Payment
from .forms import PPUserCreationForm

class TestAccountsModels(TestCase):
    """ Tests for accounts models """

    def test_ppuser_subscription_status(self):
        """ Create a user and test subscription status """
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
        payment = Payment(amount=5, user=user)
        payment.save()
        self.assertEqual(payment.amount, 5)
        self.assertEqual(payment.user, PPUser.objects.get(pk=1))
        self.assertEqual(str(payment), "Payment of £5 for user 1")

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

    def test_account_view(self):
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

class TestAccountForms(TestCase):
    """ Tests for account forms """    

    def test_PPUserCreationForm(self):
        """ Test creating and saving a new user form """
        form = PPUserCreationForm({'username':'testuser', 'password1':'test password', 'password2':'test password'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.save(),PPUser.objects.get(pk=1))