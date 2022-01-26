from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListRosters.as_view(), name='home'),
]