from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('create-host/', views.create_host, name='create_host'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path('tag/<slug:slug>/', views.events_by_tag, name='events_by_tag'),
    path('host/<int:host_id>/', views.events_by_host, name='events_by_host'),
]
