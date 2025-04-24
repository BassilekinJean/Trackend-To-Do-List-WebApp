from django import forms 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# class InstriptionForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class  Meta:
#         model = User
#         fields = ['username','email','password1','password2',]

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class InstriptionForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'id': 'email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nom d\'utilisateur'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirmer le mot de passe'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
