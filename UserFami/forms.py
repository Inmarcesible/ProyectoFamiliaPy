from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    imagen = forms.ImageField(required=False)

    #V31 H1:16
    class Meta:
        model = User
        #fields = ('username', 'email')
        fields = ('username', 'email', 'imagen')

