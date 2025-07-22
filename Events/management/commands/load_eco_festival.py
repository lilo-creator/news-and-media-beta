from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, time
from Events.models import Event, EventHost, EventTag, EventHighlight
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Load the Eco Future Festival 2025 event data'

    def handle(self, *args, **options):
        # Create or get the host
        host, created = EventHost.objects.get_or_create(
            name="GreenVibe Organization",
            defaults={
                'logo_url': "https://example.com/logos/greenvibe.png",
                'contact_email': "events@greenvibe.org",
                'description': "A non-profit group dedicated to environmental awareness and sustainable living."
            }
        )
        
        if created:
            self.stdout.write(f"Created host: {host.name}")
        else:
            self.stdout.write(f"Host already exists: {host.name}")

        # Create tags
        tag_names = ["Sustainability", "Festival", "Environment", "Community", "Green Living"]
        tags = []
        
        for tag_name in tag_names:
            tag, created = EventTag.objects.get_or_create(
                name=tag_name,
                defaults={
                    'slug': slugify(tag_name),
                    'color': '#28a745' if 'green' in tag_name.lower() or 'environment' in tag_name.lower() 
                            else '#007bff' if 'community' in tag_name.lower() 
                            else '#ffc107' if 'festival' in tag_name.lower()
                            else '#17a2b8'
                }
            )
            tags.append(tag)
            if created:
                self.stdout.write(f"Created tag: {tag.name}")

        # Create or update the event
        event, created = Event.objects.get_or_create(
            slug="eco-future-festival-2025",
            defaults={
                'title': "Eco Future Festival 2025",
                'description': "Join us for a vibrant celebration of sustainability, innovation, and community! Experience inspiring talks, live music, local eco-friendly vendors, and hands-on workshops that shape the future of our planet.",
                'date': datetime(2025, 8, 15).date(),
                'start_time': time(10, 0),
                'end_time': time(20, 0),
                'venue_name': "Green Park Convention Center",
                'venue_address': "123 Sustainability Avenue, Eco City, EC 45678",
                'host': host,
                'banner_image_url': "https://example.com/images/ecofuture-banner.jpg",
                'ticket_price': "Free Entry",
                'registration_link': "https://example.com/events/ecofuture/register",
                'is_featured': True,
                'is_active': True,
            }
        )
        
        if created:
            self.stdout.write(f"Created event: {event.title}")
            
            # Add tags to the event
            event.tags.set(tags)
            
            # Create event highlights
            highlights_data = [
                {
                    'title': "Keynote by Dr. Maya Fields on Renewable Energy Innovation",
                    'description': "",
                    'icon': "bi bi-mic",
                    'order': 1
                },
                {
                    'title': "Live performance by Solar Beats Band",
                    'description': "",
                    'icon': "bi bi-music-note",
                    'order': 2
                },
                {
                    'title': "Eco-market featuring over 50 local green businesses",
                    'description': "",
                    'icon': "bi bi-shop",
                    'order': 3
                },
                {
                    'title': "Interactive kids' zone with environmental games",
                    'description': "",
                    'icon': "bi bi-controller",
                    'order': 4
                }
            ]
            
            for highlight_data in highlights_data:
                EventHighlight.objects.create(
                    event=event,
                    **highlight_data
                )
            
            self.stdout.write(f"Created {len(highlights_data)} highlights for the event")
            
        else:
            self.stdout.write(f"Event already exists: {event.title}")
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded Eco Future Festival 2025 data!\n'
                f'Event URL: /events/event/{event.slug}/'
            )
        )
