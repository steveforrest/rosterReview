from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListRosters.as_view(), name='home'),
    path('roster/<int:id>/', views.RosterDetail.as_view(),
         name='roster-detail'),
    path('post-roster/', views.post_roster, name='post-roster'),
    path('accounts/', include('allauth.urls')),
    path('like/<int:id>/', views.PostLike.as_view(),
         name='like_post'),
    path('dislike/<int:id>/', views.PostDislike.as_view(),
         name='dislike_post'),
    path('update-roster/<updated_id>/', views.update_roster,
         name='update-roster'),
    path('delete-roster/<updated_id>/', views.delete_roster,
         name='delete-roster'),
]
