from django.test import TestCase

from datetime import date

from adverts.models import Advert
from boards.models import Board

class TestModels(TestCase):
    """ Tests for models """

    # Import some test data
    fixtures = ['testdata.json']

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
        """ Create a board and test for correct postCodeDistrict, name and dateActive (today) """
        board = Board(postCodeDistrict="AB123", name="Test Town")
        self.assertEqual(str(board), 'AB123')
        self.assertEqual(board.name, 'Test Town')
        board.save()
        self.assertEqual(board.dateActive, date.today())