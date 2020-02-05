from django.forms import ModelForm, ModelChoiceField, TextInput, Select

from .models import Board, PostCodeDistrict

class BoardForm(ModelForm):

    # Limit postCodeDistrict choices to those that don't already have a board
    queryset = PostCodeDistrict.objects.filter(board=None)
    postCodeDistrict = ModelChoiceField(queryset=queryset, empty_label="Select a postcode...")

    class Meta:
        model = Board
        fields = ['postCodeDistrict', 'name']
        widgets = {
            'name' : TextInput(attrs={'class':'input'}),
        }