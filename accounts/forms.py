from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UserCreationForm
from django.forms import EmailInput, TextInput

from .models import PPUser

class PPAuthenticationForm(AuthenticationForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['username'].label = 'Email'
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

class PPUserCreationForm(UserCreationForm):
    # Add bulma classes to form input fields
    def __init__(self, *args, **kwargs):
        super(PPUserCreationForm, self).__init__(*args, **kwargs)        
        self.fields['password1'].widget.attrs['class'] = 'input is-primary'
        self.fields['password2'].widget.attrs['class'] = 'input is-primary'
    # Override user model and enforce email for username
    class Meta(UserCreationForm.Meta):
        model = PPUser
        fields = ['username','first_name']
        widgets = {
            'username' : EmailInput(attrs={'class':'input is-primary'}),
            'first_name' : TextInput(attrs={'class':'input', 'placeholder':"Or nickname, we don't mind..."})           
        }
        labels = {
            'username' : 'Email'
        }