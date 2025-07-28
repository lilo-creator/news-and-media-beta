from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path('tag/<slug:slug>/', views.events_by_tag, name='events_by_tag'),
    path('host/<int:host_id>/', views.events_by_host, name='events_by_host'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
    path('debug/', views.event_debug, name='event_debug'),
    path('simple/', views.event_list_simple, name='event_list_simple'),
    # Add enhanced views as alternatives
    path('enhanced/', views.event_list, name='event_list_enhanced'),
]
