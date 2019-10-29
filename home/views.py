from django.shortcuts import render
from adverts.views import get_ads
from boards.views import get_active_board_list

def home(request):
    """ Generate Application Home Page """
    return render(request, 'home.html', {'page_title':"Welcome To Purple Pages", 'ads': get_ads(123) })

def notice_boards(request):
    """ Generate Notice Boards Page """
    return render(request, 'notice_boards.html', {'page_title':"Find Your Local Notice Board", 'active_board_list': get_active_board_list() })