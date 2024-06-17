from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    email= forms.EmailField(max_length=254)

    class Meta:
        model= User
        fields= ('username','email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control w-25 '}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-large '}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-large '}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-large '}),
        }   
        error_messages = {
            'password_mismatch': "The two password fields didn’t match.",
        }
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['password1'].error_messages['required'] = 'You must provide a password.'
                self.fields['password2'].error_messages['required'] = 'You must confirm your password.'


