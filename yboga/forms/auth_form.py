from django import forms

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """
    Форма для аутентификации пользователя
    """

    username = forms.CharField(
        label="Имя пользователя",
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль",
        max_length=20,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
