from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
