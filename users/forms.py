from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm, PasswordResetForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']


class UserPasswordResetForm(PasswordResetForm):
    to_email = User.email

    class Meta:
        model = User
        fields = ['username']
