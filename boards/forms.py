from django.forms import ModelForm, ModelChoiceField, TextInput, HiddenInput

from .models import Board, PostCodeDistrict

class BoardForm(ModelForm):

    # Limit post_code_district choices to those that don't already have a board
    queryset = PostCodeDistrict.objects.filter(board__isnull=True)
    post_code = ModelChoiceField(queryset=queryset, empty_label="Select a postcode...")

    class Meta:
        model = Board
        fields = ['name','post_code']
        widgets = {
            'name' : TextInput(attrs={'class':'input', 'placeholder':"Could be the name of the postcode town..."}),
        }
        labels = {
            'name' : "Choose a Name for this Notice Board"
        }

    # Set additional attributes of post_code
    post_code.label = 'Postcode District'
    post_code.widget.attrs['element'] = 'select'