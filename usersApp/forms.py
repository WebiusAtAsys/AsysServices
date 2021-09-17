from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

#This module will create a custom form inheriting from UserCreationForm
#The UserCreationForm will be expanded to also have an email field
#This custom form can than be imported in the views

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Asys email address'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Asys phone number'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number"]
