from django.forms import ModelForm, TextInput, Textarea, FileInput

from .models import Advert

class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        exclude = ['view_counter']
        widgets = {
            'title' : TextInput(attrs={'class':'input'}),
            'strapline' : TextInput(attrs={'class':'input'}),
            'text_content' : Textarea(attrs={'class':'textarea'}),
            'image' : FileInput(attrs={'class':'file-input', 'element':'upload'}),
        }