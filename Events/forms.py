from django import forms
from .models import Event, EventHost, EventTag, EventHighlight, EventRegistration
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'date', 'start_time', 'end_time',
            'venue_name', 'venue_address', 'host', 'banner_image',
            'banner_image_url', 'ticket_price', 'registration_link',
            'tags', 'is_featured', 'is_active'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'venue_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Venue Address'}),
            'host': forms.Select(attrs={'class': 'form-select'}),
            'banner_image': forms.FileInput(attrs={'class': 'form-control'}),
            'banner_image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Banner Image URL (optional)'}),
            'ticket_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Free Entry, $25, etc.'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Registration Link URL'}),
            'tags': forms.CheckboxSelectMultiple(),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set minimum date to today
        self.fields['date'].widget.attrs['min'] = timezone.now().date().isoformat()


class EventHostForm(forms.ModelForm):
    class Meta:
        model = EventHost
        fields = ['name', 'logo', 'logo_url', 'contact_email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization Name'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Logo URL (optional)'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@organization.com'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Organization Description'}),
        }


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (optional)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any special requirements or questions? (optional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = False
        self.fields['message'].required = False


class EventHighlightForm(forms.ModelForm):
    class Meta:
        model = EventHighlight
        fields = ['title', 'description', 'icon', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Highlight Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Description (optional)'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bootstrap Icon class (e.g., bi bi-star)'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
