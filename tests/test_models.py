from django.test import TestCase

from datetime import date

from adverts.models import Advert
from boards.models import Board, PostCodeDistrict

class TestModels(TestCase):
    """ Tests for models """

    # Import some test data
    fixtures = ['tests/testdata.json']

    def test_create_advert(self):
        """ Create an advert and test for correct title """
        advert = Advert(title='testad')
        self.assertEqual(advert.title, 'testad')

    def test_advert_to_html(self):
        """ Test that advert to_html method produces a string """
        advert = Advert.objects.get(pk=1)        
        advert_html = advert.to_html
        #self.assertTrue(isinstance(advert_html, str))

    def test_create_board(self):
        """ Create a district and board then test for correct postCodeDistrict, name and dateActive (today) """
        district = PostCodeDistrict(postcode="AAAA")
        district.save()
        board = Board(postCodeDistrict=district, name="Test Town")
        self.assertEqual(str(board), 'AAAA')
        self.assertEqual(board.name, 'Test Town')
        board.save()
        self.assertEqual(board.dateActive, date.today())