from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

User = get_user_model() # modelo do user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(
            attrs={
                'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                'placeholder': "informe o seu nome de usuário..."
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                'class': "",
                'placeholder': "senha de acesso..."
            }
        )
    )

