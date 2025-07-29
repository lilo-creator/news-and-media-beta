from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
]