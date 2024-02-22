from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
    #     attrs={'autofocus': True, 
    #             'class': 'form-control',
    #             'placeholder':'Введите ваше имя пользователя',
    #             }))
    # password = forms.CharField(label='Пароль',  widget=forms.PasswordInput(
    #     attrs={'autocomplite': 'current-password',
    #            'class': 'form-control',
    #            'placeholder':'Введите ваш пароль',
    #     }))

    class Meta:
        model = User
        fields = ('username', 'password')


