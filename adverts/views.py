from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Advert
from .forms import AdvertForm

def get_ads(board_pk):
    """ Return a tuple containing all adverts for specified board """
    all_ads = Advert.objects.filter(on_boards=board_pk)
    return tuple(all_ads)

def get_user_ads(uid):
    """ Return a tuple containing all adverts with edit frames for specified user """
    # Get the adverts
    user_ads = Advert.objects.filter(user=uid)
    # Rended each to html string with edit frame
    user_ads_html = []
    for ad in user_ads:
        user_ads_html.append(render_to_string('advert_edit_frame.html', {'ad':ad}))
    return tuple(user_ads_html)

@login_required
def advert_add_edit(request, advert_id=None):
    """ Generate add/edit page """

    def edit_advert(request, advert_id):
        """ Get and advert and pass it to add_edit page as form """
        # Get the object only if the authenticated user is that same as the adverts user
        advert = get_object_or_404(Advert, pk=advert_id, user=request.user)
        advert_form = AdvertForm(instance=advert)
        return render(request, 'advert_add_edit.html', {'page_title':'Edit Advert', 'advert_form':advert_form})

    if advert_id:
        return edit_advert(request, advert_id)
    else:
        # If a new advert create a blank form and pass this into template
        advert_form = AdvertForm()
        return render(request, 'advert_add_edit.html', {'page_title':'New Advert', 'advert_form':advert_form})