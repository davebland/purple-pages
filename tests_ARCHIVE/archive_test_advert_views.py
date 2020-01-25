from django.test import TestCase
from django.contrib.auth.models import User

from adverts.views import get_ads
from adverts.models import Advert

class TestAdvertViews(TestCase):
    """ Tests for advert views """

    # Import some test data
    fixtures = ['tests/testdata.json']

    def test_get_ads(self):
        """ Test get_ads view returns a tuple of advert objects """
        ads = get_ads(1)
        self.assertEqual(type(ads), tuple)
        for ad in ads:
            self.assertTrue(isinstance(ad, Advert))

    def test_advert_add_edit(self):
        """ Test advert_add_edit view for new or existing add returns correct template """

        # Check with non authenticated user
        new_add = self.client.get('/adverts/new', follow=True)
        self.assertTemplateUsed(new_add, 'registration/login.html')
        existing_add = self.client.get('/adverts/1/edit', follow=True)
        self.assertTemplateUsed(existing_add, 'registration/login.html')
        
        # Check with authenticated user
        self.client.login(username='pptestuser', password='localtest')
        new_add = self.client.get('/adverts/new', follow=True)
        self.assertTemplateUsed(new_add, 'advert_add_edit.html')
        existing_add = self.client.get('/adverts/1/edit', follow=True)
        self.assertTemplateUsed(existing_add, 'advert_add_edit.html')

    def test_preview_advert(self):
        """ Send a post request for advert preview and check for http response contains the posted values """
        self.client.login(username='pptestuser', password='localtest')
        post_request = self.client.post('/adverts/preview/', {'title': "test title", 'textContent': "test content", 'on_boards': 1, 'user': 1, 'template':1}) 
        self.assertEqual(post_request.status_code, 200)       
        self.assertTrue("test title" in str(post_request.content))
