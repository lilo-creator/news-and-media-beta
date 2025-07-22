from Events.models import Event, EventHost, EventTag
from datetime import date, time, timedelta

# Create or get a host
host, created = EventHost.objects.get_or_create(
    name="Local Community Center",
    defaults={
        'contact_email': 'info@community.org',
        'description': 'Community event organizer'
    }
)

# Create an event WITHOUT banner image to test placeholder
event, created = Event.objects.get_or_create(
    slug="community-workshop-no-image",
    defaults={
        'title': "Community Workshop - Web Development",
        'description': "Learn the basics of web development in this hands-on workshop. Perfect for beginners who want to start their journey in coding. We'll cover HTML, CSS, and basic JavaScript concepts.",
        'date': date.today() + timedelta(days=5),
        'start_time': time(14, 0),
        'end_time': time(17, 0),
        'venue_name': "Community Center Room A",
        'venue_address': "456 Main Street, Community Hall",
        'host': host,
        'ticket_price': "Free",
        'is_active': True,
        # Note: NOT setting banner_image or banner_image_url to test placeholder
    }
)

if created:
    print(f"✓ Created event without image: {event.title}")
    print(f"  Slug: {event.slug}")
    print(f"  URL: /events/event/{event.slug}/")
    print("This event will show the placeholder banner image.")
else:
    print(f"Event already exists: {event.title}")

print(f"Total events: {Event.objects.count()}")
