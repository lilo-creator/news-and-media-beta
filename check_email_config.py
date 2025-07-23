#!/usr/bin/env python
"""
Quick fix to use console email backend for testing
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from django.conf import settings

print("Current email configuration:")
print(f"EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")

# Check if we want to switch to console backend temporarily
print("\nTo use console email backend (emails print to terminal):")
print("1. Uncomment the console backend line in settings.py")
print("2. Comment out the SMTP backend line")
print("3. Restart the server")
