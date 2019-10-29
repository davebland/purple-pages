from django.shortcuts import render
from django.http import Http404
from django.forms.models import model_to_dict

from .models import Board
from adverts.views import get_ads

def get_active_board_list():
    """ Return a list containing properties of all active boards """
    active_board_list = []
    for board in Board.objects.all():
        # Add each board to the list as a dictionary of its properties      
        active_board_list.append(model_to_dict(board))    
    return active_board_list

def display_single_board(request, board_pk):
    """ Generate the requested notice board with all its adverts """
    try:
        board_meta = Board.objects.get(pk=board_pk)
    except:
        raise Http404("Notice board not found")
    return render(request, 'single_notice_board.html', {
        'page_title':"Notice Board",
        'board_meta' : board_meta,
        'ads': get_ads(board_pk)
        })