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
        ], widget=RadioSelect(attrs={'element':'radio'})
    )

    class Meta:
        model = Advert
        exclude = ['view_counter','image_height','image_width','active','ppuser']
        widgets = {
            'title' : TextInput(attrs={'class':'input'}),
            'strapline' : TextInput(attrs={'class':'input'}),
            'text_content' : Textarea(attrs={'class':'textarea'}),
            'image' : FileInput(attrs={'class':'file-input', 'element':'upload'}),
            'link_url' : URLInput(attrs={'class':'input'}),
            'link_text' : TextInput(attrs={'class':'input'}),
            'boards': SelectMultiple(attrs={'element':'select-multiple'}),
            'template' : RadioSelect(attrs={'element':'radio'})
        }