from django.forms import ModelForm, HiddenInput

from .models import Advert

class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'textContent', 'on_boards', 'user']
        widgets = {'user':HiddenInput()}