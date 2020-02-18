from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post, Categories

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = [
            "category",
        ]

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget())
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "subtitle",
            "content",
            "image",
            "draft",
            "publish",
            "post_category",
        ]