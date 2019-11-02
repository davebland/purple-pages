from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Advert

def get_ads(board_pk):
    """ Return a tuple containing all adverts for specified board in html form """
    all_ads = []
    for ad in Advert.objects.filter(on_boards=board_pk):
        # For each advert render its content to html string using relevant template      
        all_ads.append(render_to_string('ad_template_1.html', {'advert':ad}))
    all_ads = tuple(all_ads)
    return all_ads

def get_user_ads(uid):
    """ Return a tuple containing all adverts for specified user in html form """
    
    return render_to_string('advert_edit_frame.html', {'adverts':Advert.objects.filter(user=uid)})