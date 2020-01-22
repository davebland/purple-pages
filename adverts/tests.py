from django.test import TestCase
from django.utils import timezone

from datetime import date

from adverts.models import Advert, AdvertTemplate

class TestAdvertModels(TestCase):
    """ Tests for advert models """

    # Setup a test advert
    advert = Advert(title='Test Ad')
    advert.save()

    # Setup a test template
    template = AdvertTemplate(name="Test Template")
    template.save()

    def test_advert_title_dates(self):
        """ Test the created advert for correct title, created and modified dates """
        self.assertEqual(advert.title, 'testad')
        self.assertEqual(advert.created_date, date.today())
        self.assertEqual(advert.modified_date, date.today())

    def test_template_name_default(self):
        """ Test the created template for correct title and default template file """
        self.assertEqual(template.name, 'testad')
        self.assertEqual(template.template_file, "some rubbish")

    def test_render_advert(self):
        """ Test that advert render method produces a string """
        rendered_advert = advert.render()
        self.assertTrue(isinstance(rendered_advert, str))