from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.forms.models import model_to_dict
from django.template.loader import render_to_string

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
    """ Render a single notice board page for the requested board """
    notice_board = get_notice_board(board_pk)
    return render(request, 'notice_board_frame.html', {'page_title':"Notice Board", 'notice_board':notice_board})

def get_notice_board(board_pk):
    """ Generate html for requested notice board with all its adverts """
    # Get the details of the board or raise a 404 if it doesn't exist
    try:
        board_meta = Board.objects.get(pk=board_pk)
    except:
        raise Http404("Notice board not found")
    # Get the adverts for this board
    board_ads = get_ads(board_pk)
    # Generate the notice board html
    notice_board = render_to_string('notice_board.html',
        {
            'board_meta' : board_meta,
            'ads' : board_ads
        }
    )
    return notice_board

def set_favourite_board(request):
    """ Set favourite board pk in browser cookie and reload page """
    try:
        request.session.favourite_board
        return HttpResponse(request.session.favourite_board)
    except:
        request.session.favourite_board('test board id')
    return redirect('/board/1')