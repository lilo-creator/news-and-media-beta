from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.core.exceptions import PermissionDenied
import datetime

def is_admin_user(user):
    """Check if user is admin (superuser or staff)"""
    return user.is_authenticated and (user.is_superuser or user.is_staff)

def admin_required(function):
    """Decorator that checks if user is admin and shows custom error page if not"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not (request.user.is_superuser or request.user.is_staff):
            return render(request, 'Events/admin_required.html', status=403)
        return function(request, *args, **kwargs)
    return wrapper

def get_dummy_events():
    """Return a list of dummy events that can be used across views."""
    return [
        {
            'id': 1,
            'title': 'Tech Summit 2025',
            'slug': 'tech-summit-2025',
            'description': 'Join us for our annual tech summit featuring industry leaders discussing emerging technologies and future trends in AI, blockchain, and quantum computing. Network with fellow professionals and discover the latest innovations shaping our digital future.',
            'date': datetime.date(2025, 8, 15),
            'time': '09:00',
            'end_time': '18:00',
            'venue_name': 'Tech Convention Center',
            'venue_address': '123 Innovation Drive, San Francisco, CA',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?q=80&w=2070&auto=format&fit=crop',
            'is_featured': True,
            'is_free': False,
            'price': '$299',
            'capacity': 500,
            'registered_count': 325,
            'views_count': 1250,
            'host': {'name': 'TechCorp Inc.', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Technology'}, {'name': 'AI'}, {'name': 'Professional'}],
            'registration_link': 'https://example.com/register/tech-summit',
            'schedule': [
                {'time': '09:00 - 10:00', 'title': 'Registration & Breakfast'},
                {'time': '10:00 - 11:30', 'title': 'Keynote: Future of AI', 'speaker': 'Dr. Sarah Chen'},
                {'time': '11:45 - 13:00', 'title': 'Panel: Ethical Implications of AI', 'speaker': 'Industry Leaders'},
                {'time': '13:00 - 14:00', 'title': 'Lunch Break'},
                {'time': '14:00 - 15:30', 'title': 'Workshop: Hands-on with New Technologies'},
                {'time': '15:45 - 17:00', 'title': 'Future Trends in Tech', 'speaker': 'Michael Johnson'},
                {'time': '17:00 - 18:00', 'title': 'Networking Reception'}
            ]
        },
        {
            'id': 2,
            'title': 'Summer Music Festival',
            'slug': 'summer-music-festival-2025',
            'description': 'A weekend of amazing live music performances from local and international artists, great food, and good vibes in the heart of the city. Experience diverse musical genres and connect with music lovers from around the world.',
            'date': datetime.date(2025, 8, 20),
            'time': '14:00',
            'end_time': '23:00',
            'venue_name': 'City Park Amphitheater',
            'venue_address': '45 Park Avenue, New York, NY',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?q=80&w=2070&auto=format&fit=crop',
            'is_featured': True,
            'is_free': False,
            'price': '$75',
            'capacity': 2000,
            'registered_count': 1450,
            'views_count': 3200,
            'host': {'name': 'City Events', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Music'}, {'name': 'Entertainment'}, {'name': 'Festival'}],
            'registration_link': 'https://example.com/register/music-festival',
            'schedule': [
                {'time': '14:00 - 15:00', 'title': 'Opening Act: The Local Band'},
                {'time': '15:30 - 16:30', 'title': 'Rising Stars Performance'},
                {'time': '17:00 - 18:30', 'title': 'Indie Rock Showcase'},
                {'time': '19:00 - 20:30', 'title': 'Headliner: Electric Sound'},
                {'time': '21:00 - 23:00', 'title': 'Main Event: World-famous DJ Set'}
            ]
        },
        {
            'id': 3,
            'title': 'Contemporary Art Exhibition',
            'slug': 'contemporary-art-exhibition',
            'description': 'Explore thought-provoking works from emerging and established contemporary artists in this limited-time exhibition. Discover new perspectives and engage with innovative artistic expressions that challenge conventional boundaries.',
            'date': datetime.date(2025, 9, 5),
            'time': '10:00',
            'end_time': '19:00',
            'venue_name': 'Modern Art Gallery',
            'venue_address': '67 Culture Street, Chicago, IL',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://media.istockphoto.com/id/526927807/photo/outdoor-art-gallery-on-union-square-san-francisco.jpg?s=612x612&w=0&k=20&c=5pEW8tcAfY4Vvp7CYC8PqjFiAz4fK8kN91NJj5cCFTA=',
            'is_featured': False,
            'is_free': True,
            'price': 'Free',
            'capacity': 200,
            'registered_count': 145,
            'views_count': 850,
            'host': {'name': 'City Arts Foundation', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Art'}, {'name': 'Culture'}, {'name': 'Exhibition'}],
            'registration_link': '',
            'schedule': [
                {'time': '10:00 - 19:00', 'title': 'Exhibition Open'},
                {'time': '11:30', 'title': 'Guided Tour', 'speaker': 'Gallery Curator'},
                {'time': '14:00', 'title': 'Artist Talk', 'speaker': 'Featured Artists'},
                {'time': '16:30', 'title': 'Guided Tour', 'speaker': 'Gallery Curator'}
            ]
        },
        {
            'id': 4,
            'title': 'Business Leadership Conference',
            'slug': 'business-leadership-conference',
            'description': 'Join industry leaders and experts for a day of insightful presentations and networking opportunities focused on business growth and leadership. Learn proven strategies for scaling your business and developing your leadership skills.',
            'date': datetime.date(2025, 8, 30),
            'time': '08:30',
            'end_time': '17:00',
            'venue_name': 'Grand Hotel Conference Center',
            'venue_address': '100 Business Blvd, Boston, MA',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=2070&auto=format&fit=crop',
            'is_featured': False,
            'is_free': False,
            'price': '$199',
            'capacity': 300,
            'registered_count': 210,
            'views_count': 920,
            'host': {'name': 'Business Growth Network', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Business'}, {'name': 'Professional'}, {'name': 'Leadership'}],
            'registration_link': 'https://example.com/register/business-conference',
            'schedule': [
                {'time': '08:30 - 09:00', 'title': 'Registration & Coffee'},
                {'time': '09:00 - 10:30', 'title': 'Keynote: Future of Leadership', 'speaker': 'Amanda Rodriguez, CEO'},
                {'time': '10:45 - 12:00', 'title': 'Panel: Navigating Business Challenges'},
                {'time': '12:00 - 13:00', 'title': 'Networking Lunch'},
                {'time': '13:00 - 14:30', 'title': 'Workshop: Strategic Growth', 'speaker': 'James Wilson, Business Strategist'},
                {'time': '14:45 - 16:00', 'title': 'Innovation in Business', 'speaker': 'Dr. Raj Patel'},
                {'time': '16:00 - 17:00', 'title': 'Closing Remarks & Networking'}
            ]
        },
        {
            'id': 5,
            'title': 'Digital Marketing Masterclass',
            'slug': 'digital-marketing-masterclass',
            'description': 'Master the art of digital marketing with hands-on workshops covering SEO, social media marketing, content strategy, and analytics. Perfect for beginners and experienced marketers looking to update their skills.',
            'date': datetime.date(2025, 9, 12),
            'time': '09:00',
            'end_time': '16:00',
            'venue_name': 'Digital Hub',
            'venue_address': '456 Marketing Ave, Los Angeles, CA',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2015&auto=format&fit=crop',
            'is_featured': False,
            'is_free': False,
            'price': '$149',
            'capacity': 100,
            'registered_count': 75,
            'views_count': 650,
            'host': {'name': 'Digital Marketing Pro', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Marketing'}, {'name': 'Digital'}, {'name': 'Professional'}],
            'registration_link': 'https://example.com/register/marketing-masterclass',
            'schedule': [
                {'time': '09:00 - 10:30', 'title': 'SEO Fundamentals', 'speaker': 'John Smith'},
                {'time': '10:45 - 12:15', 'title': 'Social Media Strategy', 'speaker': 'Sarah Johnson'},
                {'time': '13:15 - 14:45', 'title': 'Content Marketing', 'speaker': 'Mike Davis'},
                {'time': '15:00 - 16:00', 'title': 'Analytics & Measurement', 'speaker': 'Lisa Chen'}
            ]
        },
        {
            'id': 6,
            'title': 'Food & Wine Festival',
            'slug': 'food-wine-festival',
            'description': 'Celebrate culinary excellence with renowned chefs, wine tastings, and gourmet food experiences. Discover new flavors, learn cooking techniques, and enjoy live entertainment in a festive atmosphere.',
            'date': datetime.date(2025, 9, 25),
            'time': '12:00',
            'end_time': '20:00',
            'venue_name': 'Riverside Park',
            'venue_address': '789 River Road, Portland, OR',
            'venue_map_url': 'https://maps.google.com',
            'banner_image_url': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=2070&auto=format&fit=crop',
            'is_featured': True,
            'is_free': False,
            'price': '$85',
            'capacity': 800,
            'registered_count': 520,
            'views_count': 1850,
            'host': {'name': 'Culinary Arts Society', 'logo_url': 'https://via.placeholder.com/150'},
            'tags': [{'name': 'Food'}, {'name': 'Entertainment'}, {'name': 'Festival'}],
            'registration_link': 'https://example.com/register/food-festival',
            'schedule': [
                {'time': '12:00 - 13:30', 'title': 'Chef Demonstrations'},
                {'time': '14:00 - 15:30', 'title': 'Wine Tasting Experience'},
                {'time': '16:00 - 17:30', 'title': 'Cooking Workshops'},
                {'time': '18:00 - 20:00', 'title': 'Live Music & Dining'}
            ]
        }
    ]

def event_list(request):
    """
    Display events page with enhanced filtering and search functionality.
    """
    events = get_dummy_events()
    
    # Search functionality
    search_query = request.GET.get('search', '').strip()
    if search_query:
        events = [
            event for event in events 
            if search_query.lower() in event['title'].lower() or 
               search_query.lower() in event['description'].lower() or
               search_query.lower() in event['venue_name'].lower() or
               any(search_query.lower() in tag['name'].lower() for tag in event['tags'])
        ]
    
    # Filter by tag if requested
    tag = request.GET.get('tag')
    if tag:
        events = [event for event in events if any(t['name'].lower() == tag.lower() for t in event['tags'])]
    
    # Filter by featured if requested
    featured_only = request.GET.get('featured')
    if featured_only:
        events = [event for event in events if event['is_featured']]
    
    # Filter by past events if requested
    past_only = request.GET.get('past')
    if past_only:
        events = [event for event in events if event['date'] < datetime.date.today()]
    
    # Sort events by date
    events.sort(key=lambda x: x['date'])
    
    context = {
        'upcoming_events': [e for e in events if e['date'] >= datetime.date.today()],
        'past_events': [e for e in events if e['date'] < datetime.date.today()],
        'featured_events': [e for e in events if e['is_featured']],
        'free_events': [e for e in events if e['is_free']],
        'tags': [
            {'name': 'Technology', 'count': 2}, 
            {'name': 'Music', 'count': 1}, 
            {'name': 'Art', 'count': 1},
            {'name': 'Business', 'count': 1},
            {'name': 'Entertainment', 'count': 1},
            {'name': 'Professional', 'count': 2}
        ],
        'current_tag': tag,
        'search_query': search_query,
        'total_events': len(events)
    }
    
    return render(request, 'Events/event_list_enhanced.html', context)

def event_detail(request, slug):
    """Display event detail page using dummy data with enhanced features."""
    events = get_dummy_events()
    event = next((e for e in events if e['slug'] == slug), None)
    
    if not event:
        raise Http404("Event not found")
    
    # Increment view count (in real implementation, this would update the database)
    event['views_count'] += 1
    
    # Get related events (with same tags)
    event_tags = [tag['name'].lower() for tag in event['tags']]
    related_events = [
        e for e in events 
        if e['id'] != event['id'] and any(tag['name'].lower() in event_tags for tag in e['tags'])
    ][:3]
    
    # Calculate registration percentage
    registration_percentage = round((event['registered_count'] / event['capacity']) * 100)
    
    context = {
        'event': event,
        'related_events': related_events,
        'registration_percentage': registration_percentage,
        'is_sold_out': event['registered_count'] >= event['capacity'],
        'spots_remaining': event['capacity'] - event['registered_count'],
    }
    
    return render(request, 'Events/event_detail_enhanced.html', context)

def events_by_tag(request, slug):
    """
    Display events filtered by tag - redirects to main event list since we're using hardcoded data.
    """
    # Just redirect to the main event list page
    return redirect('events:event_list')

def events_by_host(request, host_id):
    """
    Display events filtered by host - redirects to main event list since we're using hardcoded data.
    """
    # Just redirect to the main event list page
    return redirect('events:event_list')

def sitemap_xml(request):
    """
    Generate XML sitemap with hardcoded entries since we're using dummy data.
    """
    context = {
        # No context needed - hardcoded values in template
    }
    
    response = render(request, 'Events/sitemap.xml', context)
    response['Content-Type'] = 'application/xml'
    return response

def event_debug(request):
    """Debug view to check event data."""
    events = get_dummy_events()
    
    context = {
        'upcoming_events': [e for e in events if e['date'] >= datetime.date.today()],
        'past_events': [e for e in events if e['date'] < datetime.date.today()],
        'featured_events': [e for e in events if e['is_featured']],
    }
    
    return render(request, 'Events/event_debug.html', context)

def event_list_simple(request):
    """Simple event list view without sidebar for testing."""
    events = get_dummy_events()
    
    # Filter by tag if requested
    tag = request.GET.get('tag')
    if tag:
        events = [event for event in events if any(t['name'].lower() == tag.lower() for t in event['tags'])]
    
    context = {
        'upcoming_events': [e for e in events if e['date'] >= datetime.date.today()],
        'past_events': [e for e in events if e['date'] < datetime.date.today()],
        'featured_events': [e for e in events if e['is_featured']],
        'tags': [
            {'name': 'Technology', 'count': 2}, 
            {'name': 'Music', 'count': 1}, 
            {'name': 'Art', 'count': 1},
            {'name': 'Business', 'count': 1},
            {'name': 'Entertainment', 'count': 1},
            {'name': 'Professional', 'count': 2}
        ],
        'current_tag': tag
    }
    
    return render(request, 'Events/event_list_simple.html', context)
