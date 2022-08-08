from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import CustomUser


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "email", "nickname")
