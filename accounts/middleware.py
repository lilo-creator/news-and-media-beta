from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages

class EmailVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Paths that don't require email verification
        exempt_paths = [
            '/accounts/login/',
            '/accounts/logout/',
            '/accounts/register/',
            '/accounts/verify-email/',
            '/accounts/verify-email-required/',
            '/accounts/resend-verification/',
            '/accounts/password-reset/',
            '/accounts/password-reset-confirm/',
            '/admin/',
            '/static/',
            '/media/',
        ]

        # Check if user is authenticated and on a protected path
        if request.user.is_authenticated:
            current_path = request.path
            is_exempt = any(current_path.startswith(path) for path in exempt_paths)
            
            # Get verification status from user profile
            try:
                is_verified = request.user.emailverification.is_verified if hasattr(request.user, 'emailverification') else False
            except:
                is_verified = False

            if not is_verified and not is_exempt:
                messages.warning(
                    request,
                    "Please verify your email address to access this page. "
                    "Check your inbox for the verification link or request a new one."
                )
                return redirect('verify_email_required')

        response = self.get_response(request)
        return response
