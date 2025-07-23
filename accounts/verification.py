from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import EmailVerification
import uuid

@login_required
def verify_email_required(request):
    """Show the email verification required page"""
    if hasattr(request.user, 'emailverification') and request.user.emailverification.is_verified:
        messages.success(request, "Your email is already verified!")
        return redirect('home')
    return render(request, 'accounts/verify_email_required.html')

@login_required
def resend_verification(request):
    """Resend the verification email"""
    # Delete any existing unverified tokens
    EmailVerification.objects.filter(user=request.user, is_verified=False).delete()
    
    # Create new verification token
    verification = EmailVerification.objects.create(
        user=request.user,
        token=str(uuid.uuid4())
    )
    
    # Build the verification URL
    verify_url = request.build_absolute_uri(
        reverse('verify_email', args=[verification.token])
    )
    
    # Create email content
    context = {
        'user': request.user,
        'verify_url': verify_url
    }
    
    html_message = render_to_string('accounts/email/verify_email.html', context)
    plain_message = strip_tags(html_message)
    
    # Send the verification email
    try:
        send_mail(
            'Verify Your Email Address',
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            html_message=html_message,
            fail_silently=False,
        )
        messages.success(
            request,
            "A new verification email has been sent. Please check your inbox."
        )
    except Exception as e:
        messages.error(
            request,
            f"Failed to send verification email. Please try again later. Error: {str(e)}"
        )
    
    return redirect('verify_email_required')
