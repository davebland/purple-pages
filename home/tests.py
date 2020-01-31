from django.test import TestCase

class HomeViews(TestCase):
    """ Tests for home views models """

    def test_home_template(self):
        """ Test that the home page returns the home template """        
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'home.html')

    def test_search_template(self):
        """ Test that the search page returns the search template """        
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'search.html')
        page = self.client.get("/search/?search_string=test")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'search.html')