#!/usr/bin/env python
"""
Script to check events in the database and test the home page upcoming events functionality.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from Events.models import Event
from django.utils import timezone

def check_events():
    print("Checking events in database...")
    
    # Get all events
    all_events = Event.objects.all()
    print(f"Total events in database: {all_events.count()}")
    
    if all_events.exists():
        print("\nAll events:")
        for event in all_events:
            status = "Active" if event.is_active else "Inactive"
            upcoming = "Upcoming" if event.is_upcoming else "Past"
            print(f"- {event.title} | {event.date} | {status} | {upcoming}")
    
    # Get upcoming events (same logic as in home view)
    now = timezone.now()
    upcoming_events = Event.objects.filter(
        is_active=True,
        date__gte=now.date()
    ).order_by('date', 'start_time')[:6]
    
    print(f"\nUpcoming events for home page: {upcoming_events.count()}")
    for event in upcoming_events:
        print(f"- {event.title} | {event.date} at {event.start_time}")
        print(f"  Venue: {event.venue_name}")
        print(f"  Has banner: {bool(event.banner_image)}")
        print()

if __name__ == "__main__":
    check_events()
