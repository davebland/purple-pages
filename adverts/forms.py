from django.forms import ModelForm, TextInput, Textarea, FileInput, URLInput, ChoiceField, RadioSelect, SelectMultiple

from .models import Advert

class AdvertForm(ModelForm):
    """ Form for creating or editing an advert object """

    background_color_class = ChoiceField(choices=[
            ('white','white'),
            ('black','black'),
            ('primary','primary'),
            ('info','info'),
            ('link','link'),
            ('success','success'),
            ('warning','warning'),
            ('danger','danger'),
        ], label="Background Color", widget=RadioSelect(attrs={'element':'radio'})
    )

    class Meta:
        model = Advert
        exclude = ['view_counter','image_height','image_width','active']
        widgets = {
            'title' : TextInput(attrs={'class':'input is-primary', 'placeholder':"Make it short and catchy..."}),
            'strapline' : TextInput(attrs={'class':'input', 'placeholder':"Draw them in"}),
            'text_content' : Textarea(attrs={'class':'textarea', 'placeholder':"The detail..."}),
            'image' : FileInput(attrs={'class':'file-input', 'element':'upload'}),
            'link_url' : URLInput(attrs={'class':'input', 'placeholder':"Remember to use the full https://..."}),
            'link_text' : TextInput(attrs={'class':'input', 'placeholder':"Keep it short or leave empty"}),
            'boards': SelectMultiple(attrs={'element':'select-multiple'}),
            'template' : RadioSelect(attrs={'element':'radio'})
        }
        labels = {
            'text_content': "Main Text",
            'link_url': "Link URL",
            'link_text': "Link Text",
            'boards': "Notice Boards (1 or more)"
        }