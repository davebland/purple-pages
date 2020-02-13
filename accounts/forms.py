from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

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

class PPSetPasswordForm(SetPasswordForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'input'
        self.fields['new_password2'].widget.attrs['class'] = 'input'

class PPPasswordChangeForm(PasswordChangeForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'input'
        self.fields['new_password1'].widget.attrs['class'] = 'input'
        self.fields['new_password2'].widget.attrs['class'] = 'input'