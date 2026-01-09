from django.forms import ModelForm
from .models import NewItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewItemForm(ModelForm):
    class Meta:
        model = NewItem
        fields = ['category','name','photo','description','price']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')