from django.urls import path
from .views import article_detail

urlpatterns = [
    path('article/<str:sport>/', article_detail, name='article_detail'),
]
