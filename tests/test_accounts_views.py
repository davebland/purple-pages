from django.test import TestCase

class TestAccountViews(TestCase):
    """ Tests for account views """

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