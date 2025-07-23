"""
Custom email backend with detailed logging
"""
import logging
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('django.mail')

class LoggingEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.info(f"📧 Email Configuration:")
        logger.info(f"HOST: {settings.EMAIL_HOST}")
        logger.info(f"PORT: {settings.EMAIL_PORT}")
        logger.info(f"TLS: {settings.EMAIL_USE_TLS}")
        logger.info(f"FROM: {settings.DEFAULT_FROM_EMAIL}")
        # Don't log the full password
        logger.info(f"USER: {settings.EMAIL_HOST_USER}")
        if settings.EMAIL_HOST_PASSWORD:
            logger.info("PASSWORD: [Set]")
        else:
            logger.info("PASSWORD: [Not Set]")

    def open(self):
        """Logging the connection attempt"""
        try:
            logger.info("🔄 Attempting to connect to email server...")
            connected = super().open()
            if connected:
                logger.info("✅ Successfully connected to email server!")
            else:
                logger.error("❌ Failed to connect to email server")
            return connected
        except Exception as e:
            logger.error(f"❌ Error connecting to email server: {str(e)}")
            raise

    def send_messages(self, email_messages):
        """Logging the sending of messages"""
        if not email_messages:
            logger.warning("⚠️ No email messages to send")
            return 0

        logger.info(f"📨 Attempting to send {len(email_messages)} message(s)...")
        
        try:
            num_sent = super().send_messages(email_messages)
            if num_sent:
                logger.info(f"✅ Successfully sent {num_sent} message(s)!")
                for message in email_messages:
                    logger.info(f"📧 Sent email:")
                    logger.info(f"   To: {message.to}")
                    logger.info(f"   Subject: {message.subject}")
            else:
                logger.error("❌ No messages were sent")
            return num_sent
        except Exception as e:
            logger.error(f"❌ Error sending email: {str(e)}")
            logger.error("Debug information:")
            logger.error(f"- Host: {settings.EMAIL_HOST}")
            logger.error(f"- Port: {settings.EMAIL_PORT}")
            logger.error(f"- TLS: {settings.EMAIL_USE_TLS}")
            logger.error(f"- Username: {settings.EMAIL_HOST_USER}")
            # Check if password has spaces
            if settings.EMAIL_HOST_PASSWORD and ' ' in settings.EMAIL_HOST_PASSWORD:
                logger.error("⚠️ WARNING: Email password contains spaces! Gmail app passwords should not have spaces.")
            raise
