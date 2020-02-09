from django.contrib.auth.forms import AuthenticationForm 

class PPAuthenticationForm(AuthenticationForm):

    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['class'] = 'input'
    