from django.test import TestCase
from adverts.views import get_ads
from boards.views import get_active_board_list

class TestViews(TestCase):
    """ Tests for views """

    # Import some test data
    fixtures = ['testdata.json']

    def test_get_home_page(self):
        """ Get home page and test for successful response and correct template """ 
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'home.html')

    def test_get_notice_board_page(self):
        """ Get notice board page and test for successful response and correct templates """ 
        page = self.client.get("/boards")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'notice_boards.html')

    def test_get_ads(self):
        """ Test get_ads view returns a tuple of strings """
        ads = get_ads(1)
        self.assertEqual(type(ads), tuple)
        for ad in ads:
            self.assertTrue(isinstance(ad, str))

    def test_get_active_board_list(self):
        """ Test get_active_board_list view returns a list of dictionaries """
        boards = get_active_board_list()
        self.assertEqual(type(boards), list)      
        for board in boards:
            self.assertTrue(isinstance(board, dict))

    def test_display_single_board(self):
        """ Get a single notice board page and test for successful response and correct base templates """ 
        page = self.client.get("/boards/1/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'notice_board_frame.html')
        self.assertTemplateUsed(page, 'notice_board.html')