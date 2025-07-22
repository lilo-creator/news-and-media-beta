from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Event, EventTag, EventHost, EventRegistration
from .forms import EventForm, EventHostForm, EventRegistrationForm

def event_list(request):
    """Display all active events."""
    events = Event.objects.filter(is_active=True)
    
    # Filter by tag
    tag_slug = request.GET.get('tag')
    if tag_slug:
        events = events.filter(tags__slug=tag_slug)
    
    # Filter upcoming/past events
    filter_type = request.GET.get('filter')
    if filter_type == 'upcoming':
        events = events.filter(date__gte=timezone.now().date())
    elif filter_type == 'past':
        events = events.filter(date__lt=timezone.now().date())
    # For 'all' or no filter, show all events (no additional filtering by date)
    
    # Search
    query = request.GET.get('q')
    if query:
        events = events.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(venue_name__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get featured events for sidebar
    featured_events = Event.objects.filter(is_featured=True, is_active=True)[:3]
    
    # Get all tags for filter
    tags = EventTag.objects.all()
    
    context = {
        'page_obj': page_obj,
        'featured_events': featured_events,
        'tags': tags,
        'current_filter': filter_type,
        'current_tag': tag_slug,
        'search_query': query,
        'total_events': events.count(),
    }
    
    return render(request, 'Events/event_list.html', context)

def event_detail(request, slug):
    """Display event detail page."""
    event = get_object_or_404(Event, slug=slug, is_active=True)
    
    # Increment view count
    event.increment_views()
    
    # Handle registration form submission
    registration_form = EventRegistrationForm()
    registration_success = False
    
    if request.method == 'POST':
        registration_form = EventRegistrationForm(request.POST)
        if registration_form.is_valid():
            try:
                # Use get_or_create to handle uniqueness constraint
                registration, created = EventRegistration.objects.get_or_create(
                    event=event,
                    email=registration_form.cleaned_data['email'],
                    defaults={
                        'name': registration_form.cleaned_data['name'],
                        'phone': registration_form.cleaned_data['phone'],
                        'message': registration_form.cleaned_data['message'],
                    }
                )
                
                if created:
                    messages.success(request, 'Registration successful! You will receive a confirmation email shortly.')
                    registration_success = True
                    registration_form = EventRegistrationForm()  # Reset form
                else:
                    messages.warning(request, 'You have already registered for this event!')
                    
            except IntegrityError:
                messages.error(request, 'Registration failed due to a database error. You may have already registered for this event.')
            except Exception as e:
                messages.error(request, 'An unexpected error occurred during registration. Please try again.')
    
    # Get related events (same tags or host)
    related_events = Event.objects.filter(
        is_active=True,
        date__gte=timezone.now().date()
    ).filter(
        Q(tags__in=event.tags.all()) | Q(host=event.host)
    ).exclude(id=event.id).distinct()[:4]
    
    context = {
        'event': event,
        'related_events': related_events,
        'registration_form': registration_form,
        'registration_success': registration_success,
    }
    
    return render(request, 'Events/event_detail.html', context)

@login_required
def create_event(request):
    """Create a new event."""
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            # Generate slug from title
            event.slug = slugify(event.title)
            
            # Ensure unique slug
            counter = 1
            original_slug = event.slug
            while Event.objects.filter(slug=event.slug).exists():
                event.slug = f"{original_slug}-{counter}"
                counter += 1
            
            event.save()
            form.save_m2m()  # Save many-to-many relationships
            
            messages.success(request, f'Event "{event.title}" created successfully!')
            return redirect('events:event_detail', slug=event.slug)
    else:
        form = EventForm()
    
    context = {
        'form': form,
        'title': 'Create New Event'
    }
    
    return render(request, 'Events/create_event.html', context)

@login_required
def create_host(request):
    """Create a new event host/organization."""
    if request.method == 'POST':
        form = EventHostForm(request.POST, request.FILES)
        if form.is_valid():
            host = form.save()
            messages.success(request, f'Organization "{host.name}" created successfully!')
            return redirect('events:event_list')
    else:
        form = EventHostForm()
    
    context = {
        'form': form,
        'title': 'Add New Organization'
    }
    
    return render(request, 'Events/create_host.html', context)

def events_by_tag(request, slug):
    """Display events filtered by tag."""
    tag = get_object_or_404(EventTag, slug=slug)
    events = Event.objects.filter(tags=tag, is_active=True, date__gte=timezone.now().date())
    
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'tag': tag,
        'page_obj': page_obj,
    }
    
    return render(request, 'Events/events_by_tag.html', context)

def events_by_host(request, host_id):
    """Display events filtered by host."""
    host = get_object_or_404(EventHost, id=host_id)
    events = Event.objects.filter(host=host, is_active=True, date__gte=timezone.now().date())
    
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'host': host,
        'page_obj': page_obj,
    }
    
    return render(request, 'Events/events_by_host.html', context)
