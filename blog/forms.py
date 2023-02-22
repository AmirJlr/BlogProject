from django import forms
from .models import Comment


class ShareForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
