from django.test import TestCase

class TestViews(TestCase):
    """ Tests for views """
    def test_get_home_page(self):
        """ Get home page and test for successful response and correct template """ 
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'home.html')

    def test_get_notice_board_page(self):
        """ Get notice board page and test for successful response and correct template """ 
        page = self.client.get("/boards/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'base.html')
        self.assertTemplateUsed(page, 'notice_boards.html')