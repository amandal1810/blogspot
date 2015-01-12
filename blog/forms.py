from django import forms
from blog import models

class CommentForm(forms.Form):
    author = forms.CharField(label='Name', 
    						widget=forms.TextInput(attrs={'placeholder':'enter your name here'}),
    						max_length=40,
    						required=True)
    body = forms.CharField(label='Comment', 
    						widget=forms.Textarea(attrs={'placeholder':'enter your comment here'}), 
    						required=True)

    def clean_author(self):
        return self.cleaned_data.get("author") or "Anonymous"