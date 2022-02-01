from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListRosters.as_view(), name='home'),
    path('<int:id>/details/', views.roster_detail, name='roster-detail'),
]