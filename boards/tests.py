from django.test import TestCase

from datetime import date

from boards.models import PostCodeDistrict, Board
from boards.forms import BoardForm
from accounts.models import PPUser

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

    # Import a test board and postcode district
    fixtures = ['boards/fixtures/test_board.json', 'boards/fixtures/default_postcode.json']

    def test_notice_boards(self):
        """ Test that board root returns notice boards template """
        page = self.client.get("/boards/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "notice_boards.html")

    def test_single_notice_board(self):
        """ Test getting a single notice board page works for our test board and raises 404 for no board """ 
        page = self.client.get("/boards/1/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'single_notice_board.html')
        page = self.client.get("/boards/2/")
        self.assertEqual(page.status_code, 404)

    def test_create_notice_board(self):
        """ Test create notice board view returns correct template on get or post """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Test get and post to view
        page = self.client.get("/boards/create_board/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'create_notice_board.html')
        page = self.client.post("/boards/create_board/", {})
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'create_notice_board.html')

    def test_set_unset_favourite_board_session(self):
        """ Test set_favourite_board sets/unsets favourite_board in session """
        # Set favourite and test
        page = self.client.get("/boards/1/set_as_favourite/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(self.client.session['favourite_board'], 1)
        # Unset favourite and test
        page = self.client.get("/boards/1/unset_as_favourite/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertFalse(self.client.session.__contains__('favourite_board'))

    def test_set_unset_favourite_board_user(self):
        """ Test set_favourite_board sets/unsets favourite_board in user profile """
        # Create user and login
        PPUser.objects.create_user("test","test@test.com","test")
        self.client.login(username="test", password="test")
        # Test setting favourite board
        get = self.client.get("/boards/1/set_as_favourite/", follow=True)
        self.assertEqual(get.context["user"].favourite_board, Board.objects.get(pk=1))
        # Test un-setting favourite board
        get = self.client.get("/boards/1/unset_as_favourite/", follow=True)
        self.assertEqual(get.context["user"].favourite_board, None)

class TestBoardForms(TestCase):
    """ Tests for board forms """

    # Import default district data
    fixtures = ['boards/fixtures/default_postcode.json']

    def test_board_form(self):
        """ Test creating and saving a board form """
        form = BoardForm({'name':'testboard', 'post_code':PostCodeDistrict.objects.get(pk=1)})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.save(),Board.objects.get(pk=1))