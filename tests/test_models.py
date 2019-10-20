from django.test import TestCase
from adverts.views import get_ads
from adverts.models import Advert

class TestModels(TestCase):
    """ Tests for models """
    def test_create_advert(self):
        """ Create an advert and test for correct title """
        advert = Advert(title='testad')
        self.assertEqual(advert.title, 'testad')
