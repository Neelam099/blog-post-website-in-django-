from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Comment, BlogPost



class CommentForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs=
                            {"placeholder":"Drop your comment over here", "class":"form-control", "rows":4}))
    class Meta:
        model = Comment
        fields = ['body',]
        

class PostForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter yout blog title"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Write your article"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta():
        model = BlogPost
        fields = ['title', 'body', 'show', 'image']