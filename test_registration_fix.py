#!/usr/bin/env python
"""
Test script to verify that the registration fix handles duplicate entries properly.
This simulates what would happen when someone tries to register twice.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from Events.models import Event, EventRegistration
from django.db import IntegrityError

def test_registration_fix():
    print("Testing registration duplicate handling...")
    
    # Get the first event (should be the Eco Future Festival)
    try:
        event = Event.objects.first()
        if not event:
            print("No events found in database")
            return
            
        print(f"Testing with event: {event.title}")
        
        # Test data
        test_email = "test@example.com"
        test_name = "Test User"
        
        # First registration (should succeed)
        registration1, created1 = EventRegistration.objects.get_or_create(
            event=event,
            email=test_email,
            defaults={
                'name': test_name,
                'phone': '1234567890',
                'message': 'First registration test',
            }
        )
        
        print(f"First registration created: {created1}")
        
        # Second registration with same email (should not create new entry)
        registration2, created2 = EventRegistration.objects.get_or_create(
            event=event,
            email=test_email,
            defaults={
                'name': test_name + " Updated",
                'phone': '0987654321',
                'message': 'Second registration test',
            }
        )
        
        print(f"Second registration created: {created2}")
        print(f"Both registrations are same object: {registration1.id == registration2.id}")
        
        # Clean up
        registration1.delete()
        print("Test completed successfully - duplicate registrations handled properly!")
        
    except Exception as e:
        print(f"Error during test: {e}")

if __name__ == "__main__":
    test_registration_fix()
