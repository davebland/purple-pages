from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from boards.views import get_active_board_list, get_notice_board

from adverts.models import Advert

def home(request):
    """ Generate Purple Pages Home Page """
    # If favourite_board in user or session return that board rather than default content
    
    if request.user.is_authenticated and request.user.ppuser.favourite_board:
        favourite_notice_board = get_notice_board(request.user.ppuser.favourite_board.pk)
    elif 'favourite_board' in request.session:
        favourite_notice_board = get_notice_board(request.session['favourite_board'])
    else:
        favourite_notice_board = None
    
    return render(request, 'home.html', {'page_title':"Welcome To Purple Pages", 'favourite_notice_board': favourite_notice_board })

def search(request):
    """ Generate a blank search page or return results """
    adverts = None
    if 'search_string' in request.GET:
        if request.GET['search_string'] != "":
            adverts = Advert.objects.filter(Q(title__icontains=request.GET['search_string']) |
                        Q(strapline__icontains=request.GET['search_string']) |
                            Q(text_content__icontains=request.GET['search_string']) |
                                Q(link_url__icontains=request.GET['search_string']))
    return render(request, 'search.html', {'adverts':adverts})