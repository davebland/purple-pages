from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Advert

def get_ads():
    """ Return a tuple containing all adverts in html """
    all_ads = []
    for ad in Advert.objects.all():
        # For each advert render its content to html string using relevant template      
        all_ads.append(render_to_string('ad_template_1.html', {'advert':ad}))
    all_ads = tuple(all_ads)
    return all_ads