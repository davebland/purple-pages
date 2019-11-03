from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Advert

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