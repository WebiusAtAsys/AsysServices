from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()

#This module will create a custom form inheriting from UserCreationForm
#The UserCreationForm will be expanded to also have an email field
#This custom form can than be imported in the views

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']