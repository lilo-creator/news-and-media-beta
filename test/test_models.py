#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

try:
    from accounts.models import UserProfile, EmailVerification, PasswordResetToken
    print("All models imported successfully!")
    print(f"UserProfile fields: {[f.name for f in UserProfile._meta.fields]}")
except Exception as e:
    print(f"Error importing models: {e}")
