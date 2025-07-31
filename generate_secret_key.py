#!/usr/bin/env python
"""
Generate a secure random Django secret key.
"""
import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure random string for Django's SECRET_KEY setting."""
    chars = string.ascii_letters + string.digits + string.punctuation
    # Remove characters that might cause issues in shell environments
    chars = chars.replace('\'', '').replace('\"', '').replace('\\', '')
    
    secret_key = ''.join(secrets.choice(chars) for _ in range(length))
    return secret_key

if __name__ == '__main__':
    print("Generated Django SECRET_KEY:")
    print(generate_secret_key())
    print("\nAdd this to your .env file or Railway environment variables.")
