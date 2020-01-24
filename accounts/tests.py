from django.test import TestCase

from datetime import date

from accounts.models import PPUser, Payment

class TestAccountsModels(TestCase):
    """ Tests for accounts models """

    # Import default user data
    #fixtures = ['adverts/fixtures/default_user.json']

    def test_PPUser_fav_board(self):
        """ Create a user and test subscription status """
        user = PPUser()
        user.save()
        self.assertEqual(user.subscription_status(), 'Some rubbish')