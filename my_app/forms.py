from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'photo', 'password1', 'password2')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your First Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Last Name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    photo = forms.ImageField(required=False)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))