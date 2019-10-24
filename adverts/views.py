from django.shortcuts import render
from .models import Advert

def get_ads():
    """ Return a tuple containing all adverts """
    all_ads = tuple(Advert.objects.all())
    return all_ads