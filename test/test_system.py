#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from accounts.models import UserProfile
from django.contrib.auth.models import User

# Test if models work
print("Testing models...")
print(f"User model: {User}")
print(f"UserProfile model: {UserProfile}")
print(f"UserProfile fields: {[f.name for f in UserProfile._meta.fields]}")

# Test database connection
try:
    user_count = User.objects.count()
    profile_count = UserProfile.objects.count()
    print(f"Current users in database: {user_count}")
    print(f"Current profiles in database: {profile_count}")
    print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database error: {e}")

print("All tests completed!")
