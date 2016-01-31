from django import forms


from .models import Post


class PostForm(forms.ModelForm):
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