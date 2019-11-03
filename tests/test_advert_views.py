from django.test import TestCase

from adverts.views import get_ads
from adverts.models import Advert

class TestAdvertViews(TestCase):
    """ Tests for advert views """

    # Import some test data
    fixtures = ['testdata.json']

    def test_get_ads(self):
        """ Test get_ads view returns a tuple of advert objects """
        ads = get_ads(1)
        self.assertEqual(type(ads), tuple)
        for ad in ads:
            self.assertTrue(isinstance(ad, Advert))

    def test_advert_add_edit(self):
        """ Test advert_add_edit view for new or existing add returns correct template """
        new_add = self.client.get('/adverts/new', follow=True)
        self.assertTemplateUsed(new_add, 'advert_add_edit.html')
        existing_add = self.client.get('/adverts/1/edit', follow=True)
        self.assertTemplateUsed(existing_add, 'advert_add_edit.html')