from django.forms import ModelForm, HiddenInput

from .models import Advert

class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        exclude = ['impression_counter']
        widgets = {'user':HiddenInput()}