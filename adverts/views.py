from django.shortcuts import render

def get_ads():
    """ Return a dictionary of adverts """
    return {'ad1':'detail1','ad2':'detail2', 'ad3':'detail3','ad4':'detail4'}