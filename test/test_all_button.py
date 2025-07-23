#!/usr/bin/env python
"""
Test script to verify the 'All' button fix in Events app.
This script will create some test events and verify the filtering works correctly.
"""

import os
import sys
import django
from datetime import date, timedelta, time

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from Events.models import Event, EventHost
from django.test import Client
from django.urls import reverse

def test_all_button_fix():
    print("Testing Events 'All' button functionality...")
    
    # Create a test host if none exists
    host, created = EventHost.objects.get_or_create(
        name="Test Host",
        defaults={
            'contact_email': 'test@example.com',
            'description': 'Test host for button testing'
        }
    )
    
    if created:
        print("✓ Created test host")
    
    # Create test events with different dates
    today = date.today()
    
    # Past event
    past_event, created = Event.objects.get_or_create(
        slug="past-event-test",
        defaults={
            'title': "Past Event Test",
            'description': "A test event in the past",
            'date': today - timedelta(days=10),
            'start_time': time(14, 0),
            'end_time': time(18, 0),
            'venue_name': "Test Venue",
            'venue_address': "123 Test Street",
            'host': host,
            'is_active': True
        }
    )
    
    # Upcoming event
    future_event, created = Event.objects.get_or_create(
        slug="future-event-test",
        defaults={
            'title': "Future Event Test",
            'description': "A test event in the future",
            'date': today + timedelta(days=10),
            'start_time': time(14, 0),
            'end_time': time(18, 0),
            'venue_name': "Test Venue",
            'venue_address': "123 Test Street",
            'host': host,
            'is_active': True
        }
    )
    
    print(f"✓ Test events ready (past: {past_event.date}, future: {future_event.date})")
    
    # Test the filtering logic
    client = Client()
    
    # Test All filter (should show both events)
    print("\n--- Testing 'All' filter ---")
    response = client.get(reverse('events:event_list'))
    events_count = len(response.context['page_obj'])
    print(f"All events (no filter): {events_count} events")
    print(f"Filter type: {response.context.get('current_filter', 'None (correct for All)')}")
    
    # Test Upcoming filter
    print("\n--- Testing 'Upcoming' filter ---")
    response = client.get(reverse('events:event_list') + '?filter=upcoming')
    upcoming_count = len(response.context['page_obj'])
    print(f"Upcoming events: {upcoming_count} events")
    print(f"Filter type: {response.context.get('current_filter')}")
    
    # Test Past filter
    print("\n--- Testing 'Past' filter ---")
    response = client.get(reverse('events:event_list') + '?filter=past')
    past_count = len(response.context['page_obj'])
    print(f"Past events: {past_count} events")
    print(f"Filter type: {response.context.get('current_filter')}")
    
    # Verify the fix worked
    total_test_events = Event.objects.filter(slug__in=['past-event-test', 'future-event-test']).count()
    
    print(f"\n--- Results Summary ---")
    print(f"Expected: All filter shows all events ({total_test_events} or more)")
    print(f"Actual: All filter shows {events_count} events")
    print(f"Expected: Upcoming shows 1+ events, Past shows 1+ events")
    print(f"Actual: Upcoming={upcoming_count}, Past={past_count}")
    
    if events_count >= total_test_events and upcoming_count >= 1 and past_count >= 1:
        print("✅ SUCCESS: All button fix is working correctly!")
    else:
        print("❌ ISSUE: All button fix may need more work")
    
    return True

if __name__ == "__main__":
    test_all_button_fix()
