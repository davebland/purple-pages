from django.shortcuts import get_object_or_404, HttpResponse
from django.forms.models import model_to_dict

from .models import Board

def get_active_board_list():
    """ Return a list containing properties of all active boards """
    active_board_list = []
    for board in Board.objects.all():
        # Add each board to the list as a dictionary of its properties      
        active_board_list.append(model_to_dict(board))    
    return active_board_list

def display_single_board(request, board_pk):
    """ Generate the requested notice board with all its adverts """
    board_meta = Board.objects.get(pk=board_pk)
    return HttpResponse(board_meta.name)