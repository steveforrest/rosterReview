from django.forms import ModelForm
from .models import RosterList, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

#create RosterList form

class RosterForm(ModelForm):
    """
    A form for a user to create a new roster
    """
    class Meta:
        model = RosterList
        fields = ('name', 'points', 'faction', 'roster')        
        widgets = {
            'roster': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }

class CommentForm(ModelForm):
    """
    A form so comments can be added to the roster
    """
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }