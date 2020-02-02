from django.test import TestCase

from datetime import date

from boards.models import PostCodeDistrict, Board

class TestBoardModels(TestCase):
    """ Tests for board models """

    # Import default district data
    fixtures = ['boards/fixtures/default_postcode.json']

    def test_post_code_district_default(self):
        """ Test the default postcode district for correct data """        
        post_code_district = PostCodeDistrict.objects.get(pk=1)
        self.assertEqual(str(post_code_district), 'AA01')

    def test_board_name_date(self):
        """ Create and test a board for correct name and active date """
        board = Board(name="Test Board", post_code=PostCodeDistrict.objects.get(pk=1))
        board.save()
        self.assertEqual(board.name, 'Test Board')
        self.assertEqual(board.date_active, date.today())

class TestBoardViews(TestCase):
    """ Tests for board views """

    def test_notice_boards(self):
        """ Test that board root returns notice boards template """
        page = self.client.get("/boards/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "notice_boards.html")

    