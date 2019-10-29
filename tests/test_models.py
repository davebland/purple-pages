from django.test import TestCase

from datetime import date

from adverts.models import Advert
from boards.models import Board

class TestModels(TestCase):
    """ Tests for models """
    def test_create_advert(self):
        """ Create an advert and test for correct title """
        advert = Advert(title='testad')
        self.assertEqual(advert.title, 'testad')

    def test_create_board(self):
        """ Create a board and test for correct postCodeDistrict, name and dateActive (today) """
        board = Board(postCodeDistrict="AB12", name="Test Town")
        self.assertEqual(str(board), 'AB12')
        self.assertEqual(board.name, 'Test Town')
        board.save()
        self.assertEqual(board.dateActive, date.today())