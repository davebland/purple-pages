from django.test import TestCase

from adverts.models import Advert
from adverts.forms import AdvertForm

class TestForms(TestCase):
    """ Tests for forms """

    # Import some test data
    fixtures = ['testdata.json']

    def test_advertForm(self):
        """ Create an advert form, bind some data and check if valid """
        advert_form = AdvertForm(instance=Advert.objects.get(pk=1))
        self.assertTrue(advert_form.is_valid)
