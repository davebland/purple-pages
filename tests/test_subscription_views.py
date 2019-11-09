from django.test import TestCase
from django.contrib.auth.models import User

class TestSubscriptionViews(TestCase):
    """ Tests for subscription views """

    # Import some test data
    fixtures = ['tests/testdata.json']

    def test_subscription_overview(self):
        """ Get subscription overview page and check for correct template """
        page = self.client.get('/subscription/', follow=True)
        self.assertTemplateUsed(page, 'registration/login.html')
        self.client.login(username="pptestuser", password="localtest")
        page = self.client.get('/subscription/', follow=True)
        self.assertTemplateUsed(page, 'subscription_overview.html')