#!/usr/bin/env python
"""
Test email sending with detailed logging
"""
import os
import sys
import django
from django.core.mail import send_mail
from django.conf import settings
import logging

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_email():
    """Send a test email with detailed logging"""
    try:
        logger.info("🚀 Starting email test...")
        logger.info("\n📧 Email Configuration:")
        logger.info(f"Backend: {settings.EMAIL_BACKEND}")
        logger.info(f"Host: {settings.EMAIL_HOST}")
        logger.info(f"Port: {settings.EMAIL_PORT}")
        logger.info(f"TLS: {settings.EMAIL_USE_TLS}")
        logger.info(f"From: {settings.DEFAULT_FROM_EMAIL}")
        logger.info(f"Username: {settings.EMAIL_HOST_USER}")
        
        # Check password
        if not settings.EMAIL_HOST_PASSWORD:
            logger.error("❌ EMAIL_HOST_PASSWORD is not set!")
            return
        if ' ' in settings.EMAIL_HOST_PASSWORD:
            logger.error("❌ EMAIL_HOST_PASSWORD contains spaces! Remove all spaces.")
            return
        
        logger.info("\n📤 Sending test email...")
        success = send_mail(
            subject='Test Email - Django News Site',
            message='This is a test email to verify the email configuration is working.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself
            fail_silently=False,
        )
        
        if success:
            logger.info("✅ Test email sent successfully!")
            logger.info(f"Check your inbox: {settings.EMAIL_HOST_USER}")
        else:
            logger.error("❌ Failed to send test email")
            
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        logger.error("\n🔧 Troubleshooting Tips:")
        logger.error("1. Check if 2-Factor Authentication is enabled")
        logger.error("2. Verify your App Password is correct (16 characters, no spaces)")
        logger.error("3. Make sure Less Secure App Access is OFF (use App Password instead)")
        logger.error("4. Try generating a new App Password")

if __name__ == '__main__':
    test_email()
