from django import forms
from django.forms import ModelForm
from .models import RosterList, Comment

#create RosterList form

class RosterForm(ModelForm):
    class Meta:
        model = RosterList
        fields = ('name', 'points', 'faction', 'roster')        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
