from .models import Comment
from django.forms import ModelForm
from django import forms

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['owner'].label = 'Name'
        self.fields['email'].label = 'E-mail'
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Leave a comment'

    class Meta:
        model = Comment
        fields = ['owner', 'email', 'body']
       
    