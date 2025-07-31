from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail'),
]