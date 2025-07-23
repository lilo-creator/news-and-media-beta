# Email Setup Instructions

## Setting up Gmail for Django Email Verification

### Step 1: Enable 2-Factor Authentication
1. Go to [Google Account Security Settings](https://myaccount.google.com/security)
2. Under "Signing in to Google," enable 2-Step Verification
3. Follow the setup process to enable 2FA

### Step 2: Generate App Password
1. After enabling 2FA, go back to [Security Settings](https://myaccount.google.com/security)
2. Under "Signing in to Google," click on "App passwords"
3. Select "Mail" as the app and "Windows Computer" as the device
4. Click "Generate"
5. Copy the 16-character app password (it will look like: `abcd efgh ijkl mnop`)

### Step 3: Update the .env file
Open the `.env` file in your project root and update these values:

```
EMAIL_HOST_USER=your-actual-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-character-app-password
DEFAULT_FROM_EMAIL=your-actual-email@gmail.com
```

### Step 4: Test Email Configuration
Run the test script to verify everything works:
```bash
python test_email.py
```

### Alternative Email Providers

If you don't want to use Gmail, here are other popular options:

#### Outlook/Hotmail
```python
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

#### Yahoo Mail
```python
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

#### SendGrid (Recommended for production)
```python
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

### Security Notes
- Never commit your .env file to version control
- The .env file is already added to .gitignore
- Use environment variables in production
- Consider using a dedicated email service for production applications

### Troubleshooting
- If you get "Authentication failed" errors, double-check your app password
- If emails aren't being sent, check your spam folder
- Make sure "Less secure app access" is NOT enabled (use App Passwords instead)
- Verify your Gmail account doesn't have any security restrictions
