from django.test import TestCase

from datetime import date

from adverts.models import Advert, AdvertTemplate
from accounts.models import PPUser

class TestAdvertModels(TestCase):
    """ Tests for advert models """

    # Import default template data
    fixtures = ['adverts/fixtures/default_template.json']

    def test_advert_title_dates(self):
        """ Test the created advert for correct title, created and modified dates """
        # Create a test user
        test_user = PPUser()
        test_user.save()
        # Setup a test advert
        advert = Advert(title='Test Ad', ppuser=test_user)
        advert.save()
        self.assertEqual(str(advert), 'Test Ad')
        self.assertEqual(advert.created_date, date.today())
        self.assertEqual(advert.modified_date, date.today())

    def test_template_name_default(self):
        """ Test the default template for correct title and default template file """
        template = AdvertTemplate.objects.get(pk=1)
        self.assertEqual(str(template), 'default_template')
        self.assertEqual(template.template_file, "ad_template_1.html")

    def test_render_advert(self):
        """ Test that advert render method produces a string and increases view count """
        # Create a test user
        test_user = PPUser()
        test_user.save()
        # Setup a test advert
        advert = Advert(title='Test Ad', ppuser=test_user)
        advert.save()
        view_count_before = advert.view_counter
        rendered_advert = advert.render()
        view_count_after = advert.view_counter
        self.assertTrue(isinstance(rendered_advert, str))
        self.assertEqual(view_count_after, view_count_before + 1)

class TestAdvertViews(TestCase):
    """ Tests advert views """

    # Import some test data
    fixtures = ['adverts/fixtures/default_template.json',                
                'boards/fixtures/test_board.json',
                'boards/fixtures/default_postcode.json']

    def test_advert_add_edit_view(self):
        """ Test add edit view returns correct template """
        # Create user and login
        user = PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Create an advert for this user and save
        ad = Advert(title="test ad", ppuser=user)
        ad.save()
        # Get page and test
        page = self.client.get("/adverts/new/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'advert_add_edit.html')       
        page = self.client.get("/adverts/{}/edit/".format(ad.pk), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'advert_add_edit.html')

    def test_advert_preview_view(self):
        """ Test Preview returns successful if valid form data is supplied """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Make post request with invalid data
        page = self.client.post("/adverts/preview/", {'sadsad':'asdsasd'})
        self.assertEqual(page.status_code, 400)
        # Make post request with valid data
        page = self.client.post("/adverts/preview/", {'title':'test','template':1,'background_color_class':'warning','boards':1})
        self.assertEqual(page.status_code, 200)
          