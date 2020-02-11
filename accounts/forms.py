from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class PPAuthenticationForm(AuthenticationForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['class'] = 'input'

class PPPasswordResetForm(PasswordResetForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'input'