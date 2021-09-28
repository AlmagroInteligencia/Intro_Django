from django import forms
from django.forms.models import ModelForm

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')
        