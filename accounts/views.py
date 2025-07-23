from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.contrib.auth.tokens import default_token_generator
import uuid

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm, ChangePasswordForm
from .profile_forms import UserProfileForm
from .models import EmailVerification, PasswordResetToken

@login_required
def verify_email_required(request):
    """Show the email verification required page"""
    if not request.user.is_authenticated:
        return redirect('accounts:login')
        
    # Check if already verified
    try:
        if request.user.emailverification.is_verified:
            messages.success(request, "Your email is already verified!")
            return redirect('home')
    except EmailVerification.DoesNotExist:
        pass
        
    return render(request, 'accounts/verify_email_required.html')

def verify_email(request, token):
    """Handle email verification"""
    try:
        verification = EmailVerification.objects.get(token=token, is_verified=False)
        verification.is_verified = True
        verification.save()
        
        messages.success(
            request,
            "Thank you! Your email has been verified. You now have full access to your account."
        )
        return redirect('home')
        
    except EmailVerification.DoesNotExist:
        messages.error(
            request,
            "Invalid or expired verification link. Please request a new one."
        )
        return redirect('accounts:verify_email_required')


@login_required
def profile_view(request):
    """Display user profile"""
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': request.user.profile
    })


@login_required
def edit_profile_view(request):
    """Edit user profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user.profile, user=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user but don't commit yet
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            # Create verification record
            verification_token = str(uuid.uuid4())
            EmailVerification.objects.create(
                user=user,
                token=verification_token,
                is_verified=False
            )

            # Build the verification URL
            verification_url = request.build_absolute_uri(
                reverse('accounts:verify_email', args=[verification_token])
            )

            # Prepare and send verification email
            subject = 'Verify Your Email - News & Media Site'
            html_message = render_to_string('accounts/email/verify_email.html', {
                'user': user,
                'verify_url': verification_url,
            })
            plain_message = strip_tags(html_message)

            try:
                # Send verification email
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    html_message=html_message,
                    fail_silently=False,
                )
                # Email sent successfully
                login(request, user)
                messages.success(request, 'Registration successful! Please check your email to verify your account.')
                return redirect('accounts:verify_email_required')
            except Exception as e:
                messages.warning(
                    request,
                    f'Account created but failed to send verification email. Error: {str(e)}'
                )
                login(request, user)
                return redirect('accounts:verify_email_required')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name}!')
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Your account is not activated. Please check your email for verification.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')


def verify_email(request, token):
    try:
        email_verification = EmailVerification.objects.get(token=token)
        
        if email_verification.is_expired():
            messages.error(request, 'Verification link has expired. Please request a new one.')
            return redirect('accounts:resend_verification')
        
        if not email_verification.is_verified:
            email_verification.is_verified = True
            email_verification.save()
            
            user = email_verification.user
            user.is_active = True
            user.save()
            
            messages.success(request, 'Your email has been verified successfully! You can now log in.')
        else:
            messages.info(request, 'Your email is already verified.')
        
        return redirect('accounts:login')
        
    except EmailVerification.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
        return redirect('accounts:login')


def resend_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            email_verification, created = EmailVerification.objects.get_or_create(user=user)
            
            if not email_verification.is_verified:
                send_verification_email(request, user, email_verification.token)
                messages.success(request, 'Verification email sent! Please check your email.')
            else:
                messages.info(request, 'Your email is already verified.')
                
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email address.')
    
    return render(request, 'accounts/resend_verification.html')


def password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                
                # Create password reset token
                reset_token = PasswordResetToken.objects.create(user=user)
                
                # Send password reset email
                send_password_reset_email(request, user, reset_token.token)
                
                messages.success(request, 'Password reset email sent! Please check your email.')
                return redirect('accounts:login')
                
            except User.DoesNotExist:
                messages.error(request, 'No user found with this email address.')
    else:
        form = CustomPasswordResetForm()
    
    return render(request, 'accounts/password_reset.html', {'form': form})


def password_reset_confirm(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token, used=False)
        
        if reset_token.is_expired():
            messages.error(request, 'Password reset link has expired. Please request a new one.')
            return redirect('accounts:password_reset')
        
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                user = reset_token.user
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                
                reset_token.used = True
                reset_token.save()
                
                messages.success(request, 'Your password has been reset successfully! You can now log in.')
                return redirect('accounts:login')
        else:
            form = ChangePasswordForm()
        
        return render(request, 'accounts/password_reset_confirm.html', {'form': form, 'token': token})
        
    except PasswordResetToken.DoesNotExist:
        messages.error(request, 'Invalid or expired password reset link.')
        return redirect('accounts:password_reset')


def send_verification_email(request, user, token):
    current_site = get_current_site(request)
    subject = 'Verify your email address'
    
    message = render_to_string('accounts/emails/verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'token': token,
        'protocol': 'https' if request.is_secure() else 'http',
    })
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
        [user.email],
        html_message=message,
        fail_silently=False,
    )


def send_password_reset_email(request, user, token):
    current_site = get_current_site(request)
    subject = 'Reset your password'
    
    message = render_to_string('accounts/emails/password_reset_email.html', {
        'user': user,
        'domain': current_site.domain,
        'token': token,
        'protocol': 'https' if request.is_secure() else 'http',
    })
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
        [user.email],
        html_message=message,
        fail_silently=False,
    )
