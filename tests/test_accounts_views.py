from django.test import TestCase
from django.contrib.auth.models import User

class TestAccountViews(TestCase):
    """ Tests for account views """

    # Setup a test user
    #User.objects.create_user('pptestuser', 'test@test.com', 'localtest')

    def test_login_view(self):
        """ Test that login view for un-authenticated user returns Http response with correct template """
        page = self.client.get("/account/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'registration/login.html')

    def test_logout_view(self):
        """ Test that logout view returns Http response with correct template """
        page = self.client.get("/account/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'home.html')

    def test_un_authenticated_account_views(self):
        """ Test that all account views return login page for a non authenticated users """
        my_account = self.client.get("/account/", follow=True)
        my_ads = self.client.get("/account/my_ads", follow=True)      
        self.assertTemplateUsed(my_account, 'registration/login.html')
        self.assertTemplateUsed(my_ads, 'registration/login.html')

    def test_authenticated_account_views(self):
        """ Test that all account views return correct page for authenticated users """
        #self.client.login(username='pptestuser', password='localtest')
        my_account = self.client.get("/account/", follow=True)
        my_ads = self.client.get("/account/my_ads", follow=True)      
        #self.assertTemplateUsed(my_account, 'my_account.html')
        #self.assertTemplateUsed(my_ads, 'my_ads.html')