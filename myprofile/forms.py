from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', "placeholder":"Enter Email"}))
    password1 = forms.CharField(label= "Password", widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Enter password"}))
    password2 = forms.CharField(label= "Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Confirm Password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', "placeholder":"Enter Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter Firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter Lastname"}))
    pic = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Say something about yourself"}))
    class Meta:
        model = UserProfile
        exclude = ['user']

