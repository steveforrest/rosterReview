from django.contrib import admin
from .models import RosterList
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RosterList)
class RosterAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')



