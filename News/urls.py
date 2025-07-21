from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='list'),
    path('article/<slug:slug>/', views.NewsDetailView.as_view(), name='detail'),
    path('category/<slug:category>/', views.NewsListView.as_view(), name='category_list'),
]
