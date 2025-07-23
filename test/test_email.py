#!/usr/bin/env python
"""
Test script to send a verification email.
Before running this script, make sure to:
1. Update the .env file with your actual email credentials
2. Enable 2-factor authentication on your Gmail account
3. Generate an App Password for your Gmail account
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email():
    try:
        # Test sending an email
        subject = 'Test Email - News & Media Beta'
        message = 'This is a test email to verify that email sending is working properly.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]  # Send to yourself for testing
        
        print(f"Attempting to send email...")
        print(f"From: {from_email}")
        print(f"To: {recipient_list}")
        print(f"Subject: {subject}")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        print("✅ Email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("\nPlease check:")
        print("1. Your .env file has correct email credentials")
        print("2. You're using a Gmail App Password (not your regular password)")
        print("3. 2-factor authentication is enabled on your Gmail account")

if __name__ == '__main__':
    test_email()
