from django.contrib.auth.forms import AuthenticationForm

class PPAuthenticationForm(AuthenticationForm):
    pass
    #def __init__(self, *args, **kwargs):
    #fields['username'].widget.attrs['element'] = 'select'
    # Add bulma classes to form input fields
    