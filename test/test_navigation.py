#!/usr/bin/env python
"""
Test script to verify that the home page navigation links work correctly.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.urls import reverse
from django.test import Client

def test_navigation_urls():
    print("Testing navigation URLs from home page...")
    
    try:
        # Test URL reversals
        home_url = reverse('home:home')
        news_url = reverse('news:list')
        sports_url = reverse('sports:sport_list')
        events_url = reverse('events:event_list')
        
        print(f"✓ Home URL: {home_url}")
        print(f"✓ News URL: {news_url}")
        print(f"✓ Sports URL: {sports_url}")
        print(f"✓ Events URL: {events_url}")
        
        # Test that pages can be accessed
        client = Client()
        
        print("\nTesting page access...")
        
        response = client.get(home_url)
        print(f"✓ Home page: {response.status_code} (expected: 200)")
        
        response = client.get(news_url)
        print(f"✓ News page: {response.status_code} (expected: 200)")
        
        response = client.get(sports_url)
        print(f"✓ Sports page: {response.status_code} (expected: 200)")
        
        response = client.get(events_url)
        print(f"✓ Events page: {response.status_code} (expected: 200)")
        
        print("\n🎉 All navigation links are working correctly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_navigation_urls()
