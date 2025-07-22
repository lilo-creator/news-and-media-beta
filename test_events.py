from Events.models import Event, EventHost, EventTag
from datetime import date, time, timedelta

# Check existing events
print(f"Current events: {Event.objects.count()}")

# Create a host if none exists
if not EventHost.objects.exists():
    host = EventHost.objects.create(
        name="Sample Events Inc.",
        contact_email="info@sampleevents.com", 
        description="Sample event organizer"
    )
    print("Created sample host")
else:
    host = EventHost.objects.first()
    print(f"Using existing host: {host.name}")

# Create a sample event with image URL
if Event.objects.count() == 0:
    event = Event.objects.create(
        title="Tech Conference 2025",
        slug="tech-conference-2025",
        description="An amazing technology conference with industry leaders discussing the future of innovation.",
        date=date.today() + timedelta(days=10),
        start_time=time(9, 0),
        end_time=time(17, 0),
        venue_name="Convention Center",
        venue_address="123 Tech Street, City",
        host=host,
        banner_image_url="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&h=400&fit=crop",
        ticket_price="$100-200",
        is_active=True
    )
    print(f"Created sample event: {event.title}")
    print(f"Banner URL: {event.banner_image_url}")

print(f"Total events now: {Event.objects.count()}")
