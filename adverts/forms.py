from django.forms import ModelForm

from .models import Advert

class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'textContent', 'on_boards']