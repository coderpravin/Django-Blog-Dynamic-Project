from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
   
    password1 = forms.CharField(
        label = "Password1",
        widget=forms.PasswordInput,
        help_text=""
    )
    password2 = forms.CharField(
        label="Password2", 
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2" )