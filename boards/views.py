from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import date

from .models import Board
from adverts.models import Advert

from .forms import BoardForm

def notice_boards(request):
    """ Generate Notice Boards Page """
    return render(request, 'notice_boards.html', {'active_boards': Board.objects.all()})

def display_single_board(request, board_pk):
    """ Render a single notice board page """
    notice_board = get_object_or_404(Board, pk=board_pk)
    # Return only adverts where the owner has an active subscription
    adverts = Advert.objects.filter(boards=notice_board).filter(ppuser__subscription_expiry__gte = date.today())
    return render(request, 'single_notice_board.html', {'notice_board':notice_board, 'adverts':adverts})

def set_favourite_board(request, board_pk, set_unset=False):
    """ Set or unset favourite board in user profile or local cookie and reload page """
    if request.user.is_authenticated:
        # Set or unset favourite board in user profile
        if set_unset:
            request.user.favourite_board = Board.objects.get(pk=board_pk)           
            request.user.save()
        else:
            request.user.favourite_board = None
            request.user.save()
    else:        
        # Set or unset favourite board in local cookie
        if set_unset:
            request.session['favourite_board'] = board_pk
        else:
            if request.session.__contains__('favourite_board'):
                del request.session['favourite_board']

    return redirect('display_single_board', board_pk = board_pk)

@login_required
def create_notice_board(request):
    """ Create a notice board from list of available postcode districts or display form to do so """
    
    if request.method == "POST":
        # If for data posted, check and save
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            messages.success(request, "New notice board '{}' created.".format(board_form['name'].value()))
            return redirect('notice_boards')
        else:
            return render(request, 'create_notice_board.html', {'board_form':board_form})
    
    # Or just create a blank form and warn the user if no board can be created
    board_form = BoardForm()
    if not board_form.fields['post_code'].queryset.exists():
        messages.warning(request, 'Notice boards for all areas already exist!')
    return render(request, 'create_notice_board.html', {'board_form':board_form})