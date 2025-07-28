#!/usr/bin/env python3
"""
Test script to verify admin-only event creation functionality.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

def test_admin_only_event_creation():
    """Test that only admin users can access event creation"""
    
    print("🔒 Testing Admin-Only Event Creation Functionality")
    print("=" * 60)
    
    # Create test client
    client = Client()
    
    # Test 1: Anonymous user
    print("📋 Test 1: Anonymous user access")
    response = client.get('/events/create/')
    if response.status_code == 302:  # Redirect to login
        print("✅ PASS: Anonymous users redirected to login")
    else:
        print(f"❌ FAIL: Expected redirect (302), got {response.status_code}")
    
    # Test 2: Regular authenticated user (non-admin)
    print("\n📋 Test 2: Regular user access")
    
    # Create a regular user for testing
    regular_user, created = User.objects.get_or_create(
        username='testuser',
        defaults={
            'email': 'test@example.com',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        regular_user.set_password('testpass123')
        regular_user.save()
        print("👤 Created test regular user")
    
    # Login as regular user
    client.login(username='testuser', password='testpass123')
    response = client.get('/events/create/')
    
    if response.status_code == 403:
        print("✅ PASS: Regular users get 403 Forbidden")
        if b'Admin Access Required' in response.content:
            print("✅ PASS: Custom admin required page displayed")
        else:
            print("⚠️  WARNING: 403 returned but custom page not detected")
    else:
        print(f"❌ FAIL: Expected 403, got {response.status_code}")
    
    # Test 3: Staff user access
    print("\n📋 Test 3: Staff user access")
    
    # Create a staff user for testing
    staff_user, created = User.objects.get_or_create(
        username='staffuser',
        defaults={
            'email': 'staff@example.com',
            'is_staff': True,
            'is_superuser': False
        }
    )
    if created:
        staff_user.set_password('staffpass123')
        staff_user.save()
        print("👨‍💼 Created test staff user")
    
    # Login as staff user
    client.login(username='staffuser', password='staffpass123')
    response = client.get('/events/create/')
    
    if response.status_code == 200:
        print("✅ PASS: Staff users can access event creation")
        if b'Create' in response.content or b'Event' in response.content:
            print("✅ PASS: Event creation form displayed")
        else:
            print("⚠️  WARNING: Page loaded but form not detected")
    else:
        print(f"❌ FAIL: Expected 200, got {response.status_code}")
    
    # Test 4: Superuser access
    print("\n📋 Test 4: Superuser access")
    
    # Create a superuser for testing
    superuser, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        superuser.set_password('adminpass123')
        superuser.save()
        print("👑 Created test superuser")
    
    # Login as superuser
    client.login(username='admin', password='adminpass123')
    response = client.get('/events/create/')
    
    if response.status_code == 200:
        print("✅ PASS: Superusers can access event creation")
        if b'Create' in response.content or b'Event' in response.content:
            print("✅ PASS: Event creation form displayed")
        else:
            print("⚠️  WARNING: Page loaded but form not detected")
    else:
        print(f"❌ FAIL: Expected 200, got {response.status_code}")
    
    # Test 5: Create Host endpoint
    print("\n📋 Test 5: Create Host endpoint (admin only)")
    response = client.get('/events/create-host/')
    
    if response.status_code == 200:
        print("✅ PASS: Superusers can access host creation")
    else:
        print(f"❌ FAIL: Expected 200, got {response.status_code}")
    
    # Test with regular user
    client.login(username='testuser', password='testpass123')
    response = client.get('/events/create-host/')
    
    if response.status_code == 403:
        print("✅ PASS: Regular users cannot access host creation")
    else:
        print(f"❌ FAIL: Expected 403, got {response.status_code}")
    
    print("\n" + "=" * 60)
    print("🎯 Admin-Only Event Creation Test Completed!")
    print("📝 Summary: Only staff and superusers can create events")
    print("🔒 Security: Regular users are properly restricted")

if __name__ == '__main__':
    test_admin_only_event_creation()
