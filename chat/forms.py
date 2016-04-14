from django import forms

class ChatForm(forms.Form):
    message = forms.CharField()