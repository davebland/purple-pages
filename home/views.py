from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from datetime import date

from boards.models import Board

from adverts.models import Advert

def home(request):
    """ Generate Purple Pages Home Page """
    # If favourite_board in user or session return that board rather than default content
    favourite_notice_board = None 
    if request.user.is_authenticated and request.user.favourite_board:
        favourite_notice_board = request.user.favourite_board
    elif 'favourite_board' in request.session:
        try:
            favourite_notice_board = Board.objects.get(pk=request.session['favourite_board'])
        except:
            pass
    # If there is a favourite notice board get ads for that board
    adverts = None
    if favourite_notice_board:
        adverts = Advert.objects.filter(boards=favourite_notice_board).filter(ppuser__subscription_expiry__gte = date.today())

    return render(request, 'home.html', {'favourite_notice_board': favourite_notice_board, 'adverts':adverts })

def search(request):
    """ Generate a blank search page or return results """
    adverts = None
    if 'search_string' in request.GET:
        if request.GET['search_string'] != "":
            # Return adverts with the search_string present in any text field & filter by active subscription
            adverts = Advert.objects.filter(Q(title__icontains=request.GET['search_string']) |
                        Q(strapline__icontains=request.GET['search_string']) |
                            Q(text_content__icontains=request.GET['search_string']) |
                                Q(link_url__icontains=request.GET['search_string'])).filter(ppuser__subscription_expiry__gte = date.today())
    
    return render(request, 'search.html', {'adverts':adverts})