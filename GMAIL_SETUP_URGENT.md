# 🚨 URGENT: Gmail App Password Setup

## Current Issue
Your `.env` file still has the placeholder text `your-gmail-app-password-here` instead of an actual Gmail App Password. This is why you're getting authentication errors.

## 🔧 How to Fix This:

### Step 1: Get Gmail App Password
1. **Open Google Account Security**: https://myaccount.google.com/security
2. **Enable 2-Step Verification** (if not already enabled):
   - Click "2-Step Verification" under "Signing in to Google"
   - Follow the setup process
3. **Generate App Password**:
   - After 2FA is enabled, click "App passwords"
   - Select "Mail" as the app
   - Select "Windows Computer" as the device
   - Click "Generate"
   - **COPY the 16-character password** (example: `abcdefghijklmnop`)

### Step 2: Update .env File
Replace this line in your `.env` file:
```
EMAIL_HOST_PASSWORD=your-gmail-app-password-here
```

With your actual app password:
```
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```
(Use your actual 16-character password, not the example above)

### Step 3: Enable SMTP in Settings
After updating the .env file, uncomment the SMTP line in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Enable this
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Disable this
```

### Step 4: Restart Django Server
Stop your Django server (Ctrl+C) and start it again to load the new settings.

## 🧪 Current Temporary Fix
I've temporarily switched your email backend to console mode, so:
- **Password reset emails will now print to your terminal/console**
- **You can see the verification links in the terminal output**
- **Users can still test the registration and password reset features**

## ⚠️ Important Notes:
- **Don't use your regular Gmail password** - only use App Passwords
- **App Passwords are 16 characters** with no spaces
- **Keep the password secret** - don't share it
- **If it doesn't work**, generate a new App Password

## 🎯 Test the Current Setup:
1. Try the password reset again - emails will print to console
2. Copy the verification link from the console output
3. Paste it in your browser to test the verification process

Once you get the Gmail App Password working, you'll have real email delivery!
