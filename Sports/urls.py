
from django.urls import path, include
from . import views

app_name = 'sports'

urlpatterns = [
    path('', views.sport_list, name='sport_list'),
    path('sport/<int:pk>/', views.sport_detail, name='sport_detail'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
    path('match/<int:pk>/', views.match_detail, name='match_detail'),
    path('', include('Sports.urls_article')),
]
