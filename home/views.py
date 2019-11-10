from django.shortcuts import render

from boards.views import get_active_board_list, get_notice_board

def home(request):
    """ Generate Application Home Page """
    # If favourite_board in user or session return that board rather than default content
    
    if request.user.is_authenticated:
        favourite_notice_board = get_notice_board(request.user.ppuser.favourite_board.pk)
    elif 'favourite_board' in request.session:
        favourite_notice_board = get_notice_board(request.session['favourite_board'])
    else:
        favourite_notice_board = "No favourite set"
    
    return render(request, 'home.html', {'page_title':"Welcome To Purple Pages", 'favourite_notice_board': favourite_notice_board })

def notice_boards(request):
    """ Generate Notice Boards Page """
    return render(request, 'notice_boards.html', {'page_title':"Find Your Local Notice Board", 'active_board_list': get_active_board_list() })