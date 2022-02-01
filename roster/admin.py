from django.contrib import admin
from .models import RosterList, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RosterList)
class RosterAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(Comment)
class Comment(SummernoteModelAdmin):
    summernote_fields = ('content')
