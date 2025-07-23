#!/usr/bin/env python
"""
Gmail App Password Setup Guide and Tester
"""
import os

def print_setup_instructions():
    print("=" * 60)
    print("📧 GMAIL APP PASSWORD SETUP INSTRUCTIONS")
    print("=" * 60)
    print()
    print("1. 🔐 Enable 2-Factor Authentication:")
    print("   - Go to: https://myaccount.google.com/security")
    print("   - Under 'Signing in to Google', click '2-Step Verification'")
    print("   - Follow the setup process")
    print()
    print("2. 🔑 Generate App Password:")
    print("   - After enabling 2FA, go back to Security settings")
    print("   - Click 'App passwords' under 'Signing in to Google'")
    print("   - Select 'Mail' and 'Windows Computer'")
    print("   - Click 'Generate'")
    print("   - Copy the 16-character password (no spaces)")
    print()
    print("3. 📝 Update your .env file:")
    print("   - Replace 'your-gmail-app-password-here' with the actual password")
    print("   - Example: EMAIL_HOST_PASSWORD=abcdefghijklmnop")
    print()
    print("4. 🧪 Test the configuration:")
    print("   - Run: python test_gmail_setup.py")
    print()
    print("=" * 60)
    print("⚠️  IMPORTANT NOTES:")
    print("=" * 60)
    print("- Use the App Password, NOT your regular Gmail password")
    print("- The App Password is 16 characters with no spaces")
    print("- Keep this password secret and don't share it")
    print("- If it doesn't work, generate a new App Password")
    print()

def test_env_file():
    """Test if .env file has the required values"""
    env_path = '.env'
    
    print("🔍 Checking .env file...")
    
    if not os.path.exists(env_path):
        print("❌ .env file not found!")
        return False
    
    with open(env_path, 'r') as f:
        content = f.read()
    
    required_vars = ['EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'DEFAULT_FROM_EMAIL']
    missing_vars = []
    
    for var in required_vars:
        if var not in content:
            missing_vars.append(var)
        elif f'{var}=your-gmail-app-password-here' in content:
            print(f"⚠️  {var} still has placeholder value")
        elif f'{var}=mwaraa6@gmail.com' in content:
            print(f"✅ {var} is set correctly")
        else:
            print(f"✅ {var} is set")
    
    if missing_vars:
        print(f"❌ Missing variables: {', '.join(missing_vars)}")
        return False
    
    if 'your-gmail-app-password-here' in content:
        print("❌ Please replace 'your-gmail-app-password-here' with your actual Gmail App Password")
        return False
    
    print("✅ .env file looks good!")
    return True

def test_gmail_connection():
    """Test Gmail SMTP connection"""
    try:
        import smtplib
        
        # Read from .env file
        env_vars = {}
        with open('.env', 'r') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
        
        email = env_vars.get('EMAIL_HOST_USER', '')
        password = env_vars.get('EMAIL_HOST_PASSWORD', '')
        
        if not email or not password or password == 'your-gmail-app-password-here':
            print("❌ Please set your Gmail credentials in .env file first")
            return False
        
        print(f"🧪 Testing connection to Gmail with: {email}")
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        
        print("🎉 SUCCESS! Gmail authentication working!")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n💡 Troubleshooting:")
        print("- Make sure 2-Factor Authentication is enabled")
        print("- Generate a new App Password")
        print("- Copy the App Password exactly (16 characters, no spaces)")
        print("- Don't use your regular Gmail password")
        return False

if __name__ == '__main__':
    print_setup_instructions()
    
    if test_env_file():
        print("\n🧪 Testing Gmail connection...")
        test_gmail_connection()
    else:
        print("\n❌ Please fix the .env file first!")
