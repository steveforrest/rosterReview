from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListRosters.as_view(), name='home'),
    path('<int:id>/details/', views.RosterDetail.as_view(), name='roster-detail'),
    path('post-roster/', views.post_roster, name='post-roster'),
    path('accounts/', include('allauth.urls')),
    path('<int:id>/like/', views.PostLike.as_view(), name='like_post'),
    path('<int:id>/dislike/', views.PostDislike.as_view(), name='dislike_post'),

]