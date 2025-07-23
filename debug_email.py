#!/usr/bin/env python
"""
Debug email credentials
"""
import smtplib
from email.mime.text import MIMEText

def test_gmail_connection():
    email = 'mwaraa6@gmail.com'
    password = 'fjtyovfrrknasdxe'
    
    print(f"Testing Gmail connection with:")
    print(f"Email: {email}")
    print(f"Password length: {len(password)} characters")
    print(f"Password: {password}")
    
    try:
        # Create SMTP connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("Attempting to login...")
        server.login(email, password)
        
        print("✅ Gmail authentication successful!")
        server.quit()
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("\nPossible issues:")
        print("1. App password is incorrect")
        print("2. 2-factor authentication is not enabled")
        print("3. App password was not generated correctly")
        print("\nTo fix:")
        print("1. Go to Google Account Security")
        print("2. Enable 2-Step Verification")
        print("3. Generate a new App Password")
        print("4. Use the new 16-character password (no spaces)")
        
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == '__main__':
    test_gmail_connection()
