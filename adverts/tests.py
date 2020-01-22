from django.test import TestCase

from datetime import date

from adverts.models import Advert, AdvertTemplate

class TestAdvertModels(TestCase):
    """ Tests for advert models """

    # Import default template data
    fixtures = ['adverts/fixtures/default_template.json']

    def test_advert_title_dates(self):
        """ Test the created advert for correct title, created and modified dates """
        # Setup a test advert
        advert = Advert(title='Test Ad')
        advert.save()
        self.assertEqual(advert.title, 'Test Ad')
        self.assertEqual(advert.created_date, date.today())
        self.assertEqual(advert.modified_date, date.today())

    def test_template_name_default(self):
        """ Test the default template for correct title and default template file """
        template = AdvertTemplate.objects.get(pk=1)
        self.assertEqual(template.name, 'default_template')
        self.assertEqual(template.template_file, "ad_template_1.html")

    def test_render_advert(self):
        """ Test that advert render method produces a string and increases view count """
        # Setup a test advert
        advert = Advert(title='Test Ad')
        advert.save()
        view_count_before = advert.view_counter
        rendered_advert = advert.render()
        view_count_after = advert.view_counter
        self.assertTrue(isinstance(rendered_advert, str))
        self.assertEqual(view_count_after, view_count_before + 1)