from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from Events.models import Event, EventHost, EventTag
import random

class Command(BaseCommand):
    help = 'Create sample events with images for both past and upcoming events'

    def handle(self, *args, **options):
        # Create event hosts if they don't exist
        hosts_data = [
            {
                'name': 'City Arts Center',
                'contact_email': 'info@cityarts.com',
                'description': 'Premier arts and culture venue in the city',
                'logo_url': 'https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=200&h=200&fit=crop&crop=center'
            },
            {
                'name': 'Tech Innovation Hub',
                'contact_email': 'events@techhub.com',
                'description': 'Leading technology conference organizer',
                'logo_url': 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=200&h=200&fit=crop&crop=center'
            },
            {
                'name': 'Community Sports Club',
                'contact_email': 'contact@sportsclub.com',
                'description': 'Local sports and fitness community',
                'logo_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=200&h=200&fit=crop&crop=center'
            },
            {
                'name': 'Cultural Society',
                'contact_email': 'hello@culturalsociety.org',
                'description': 'Promoting local culture and traditions',
                'logo_url': 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=200&h=200&fit=crop&crop=center'
            }
        ]

        hosts = []
        for host_data in hosts_data:
            host, created = EventHost.objects.get_or_create(
                name=host_data['name'],
                defaults=host_data
            )
            hosts.append(host)
            if created:
                self.stdout.write(f'Created host: {host.name}')

        # Create event tags if they don't exist
        tags_data = [
            {'name': 'Music', 'slug': 'music', 'color': '#e74c3c'},
            {'name': 'Technology', 'slug': 'technology', 'color': '#3498db'},
            {'name': 'Sports', 'slug': 'sports', 'color': '#f39c12'},
            {'name': 'Art', 'slug': 'art', 'color': '#9b59b6'},
            {'name': 'Education', 'slug': 'education', 'color': '#27ae60'},
            {'name': 'Community', 'slug': 'community', 'color': '#34495e'},
            {'name': 'Business', 'slug': 'business', 'color': '#e67e22'},
            {'name': 'Health', 'slug': 'health', 'color': '#1abc9c'}
        ]

        tags = []
        for tag_data in tags_data:
            tag, created = EventTag.objects.get_or_create(
                slug=tag_data['slug'],
                defaults=tag_data
            )
            tags.append(tag)
            if created:
                self.stdout.write(f'Created tag: {tag.name}')

        # Sample events data
        events_data = [
            # Past Events
            {
                'title': 'Summer Music Festival 2024',
                'slug': 'summer-music-festival-2024',
                'description': 'A spectacular outdoor music festival featuring local and international artists. Experience three days of non-stop music, food, and entertainment in the heart of the city.',
                'date': timezone.now().date() - timedelta(days=30),
                'start_time': '18:00',
                'end_time': '23:00',
                'venue_name': 'Central Park Amphitheater',
                'venue_address': '123 Park Avenue, Downtown',
                'ticket_price': '$45 - $85',
                'banner_image_url': 'https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['music', 'community']
            },
            {
                'title': 'Tech Innovation Conference 2024',
                'slug': 'tech-innovation-conference-2024',
                'description': 'Join industry leaders and innovators as they discuss the future of technology. Network with professionals and discover the latest trends in AI, blockchain, and digital transformation.',
                'date': timezone.now().date() - timedelta(days=45),
                'start_time': '09:00',
                'end_time': '17:00',
                'venue_name': 'Convention Center Hall A',
                'venue_address': '456 Business District, Suite 100',
                'ticket_price': '$150 - $300',
                'banner_image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['technology', 'business', 'education']
            },
            {
                'title': 'Community Art Exhibition',
                'slug': 'community-art-exhibition-2024',
                'description': 'Showcasing the incredible talent of local artists. This month-long exhibition features paintings, sculptures, photography, and digital art from emerging and established creators.',
                'date': timezone.now().date() - timedelta(days=60),
                'start_time': '10:00',
                'end_time': '18:00',
                'venue_name': 'City Gallery',
                'venue_address': '789 Arts District, Gallery Row',
                'ticket_price': 'Free Entry',
                'banner_image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1200&h=600&fit=crop',
                'is_featured': False,
                'tags': ['art', 'community']
            },
            {
                'title': 'City Marathon 2024',
                'slug': 'city-marathon-2024',
                'description': 'The annual city marathon bringing together runners from around the world. Multiple categories including full marathon, half marathon, and 5K fun run for all fitness levels.',
                'date': timezone.now().date() - timedelta(days=20),
                'start_time': '07:00',
                'end_time': '14:00',
                'venue_name': 'City Hall Start/Finish Line',
                'venue_address': '321 Government Plaza',
                'ticket_price': '$25 - $75',
                'banner_image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['sports', 'health', 'community']
            },
            # Upcoming Events
            {
                'title': 'Winter Food Festival 2025',
                'slug': 'winter-food-festival-2025',
                'description': 'Celebrate the flavors of winter with local restaurants, food trucks, and specialty vendors. Cooking demonstrations, wine tastings, and live entertainment throughout the weekend.',
                'date': timezone.now().date() + timedelta(days=15),
                'start_time': '11:00',
                'end_time': '22:00',
                'venue_name': 'Waterfront Park',
                'venue_address': '555 Harbor Boulevard',
                'ticket_price': '$20 - $40',
                'banner_image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['community']
            },
            {
                'title': 'Digital Marketing Summit 2025',
                'slug': 'digital-marketing-summit-2025',
                'description': 'Learn from industry experts about the latest digital marketing strategies, social media trends, and e-commerce innovations. Workshops and networking opportunities included.',
                'date': timezone.now().date() + timedelta(days=30),
                'start_time': '08:30',
                'end_time': '16:30',
                'venue_name': 'Business Center Auditorium',
                'venue_address': '888 Corporate Drive',
                'ticket_price': '$200 - $400',
                'banner_image_url': 'https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['business', 'technology', 'education']
            },
            {
                'title': 'Spring Jazz Concert Series',
                'slug': 'spring-jazz-concert-series-2025',
                'description': 'An intimate evening of smooth jazz featuring renowned local musicians and special guest performers. Enjoy cocktails and light appetizers while listening to world-class music.',
                'date': timezone.now().date() + timedelta(days=45),
                'start_time': '19:30',
                'end_time': '22:30',
                'venue_name': 'Jazz Club Downtown',
                'venue_address': '222 Music Street',
                'ticket_price': '$35 - $60',
                'banner_image_url': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=1200&h=600&fit=crop',
                'is_featured': False,
                'tags': ['music']
            },
            {
                'title': 'Health & Wellness Expo 2025',
                'slug': 'health-wellness-expo-2025',
                'description': 'Discover the latest in health, fitness, and wellness. Free health screenings, yoga classes, nutrition workshops, and vendor booths featuring natural products and services.',
                'date': timezone.now().date() + timedelta(days=60),
                'start_time': '09:00',
                'end_time': '17:00',
                'venue_name': 'Community Center',
                'venue_address': '999 Wellness Way',
                'ticket_price': 'Free Entry',
                'banner_image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['health', 'community']
            },
            {
                'title': 'Startup Pitch Competition 2025',
                'slug': 'startup-pitch-competition-2025',
                'description': 'Watch innovative startups pitch their ideas to a panel of investors and industry experts. Networking reception follows with opportunities to meet entrepreneurs and mentors.',
                'date': timezone.now().date() + timedelta(days=20),
                'start_time': '14:00',
                'end_time': '18:00',
                'venue_name': 'Innovation Hub',
                'venue_address': '777 Entrepreneur Plaza',
                'ticket_price': '$15 - $25',
                'banner_image_url': 'https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=1200&h=600&fit=crop',
                'is_featured': False,
                'tags': ['business', 'technology']
            },
            {
                'title': 'International Film Festival',
                'slug': 'international-film-festival-2025',
                'description': 'A week-long celebration of international cinema featuring independent films, documentaries, and short films from around the world. Q&A sessions with directors and actors.',
                'date': timezone.now().date() + timedelta(days=75),
                'start_time': '18:00',
                'end_time': '23:00',
                'venue_name': 'Grand Theater',
                'venue_address': '111 Cinema Boulevard',
                'ticket_price': '$12 - $25',
                'banner_image_url': 'https://images.unsplash.com/photo-1489599611389-206364e8b31c?w=1200&h=600&fit=crop',
                'is_featured': True,
                'tags': ['art']
            }
        ]

        # Create events
        for event_data in events_data:
            # Convert string time to time objects
            start_time = datetime.strptime(event_data['start_time'], '%H:%M').time()
            end_time = datetime.strptime(event_data['end_time'], '%H:%M').time()
            
            # Extract tag names and host index
            tag_names = event_data.pop('tags')
            host_index = random.randint(0, len(hosts) - 1)
            
            event_data['start_time'] = start_time
            event_data['end_time'] = end_time
            event_data['host'] = hosts[host_index]
            
            event, created = Event.objects.get_or_create(
                slug=event_data['slug'],
                defaults=event_data
            )
            
            if created:
                # Add tags
                for tag_name in tag_names:
                    try:
                        tag = EventTag.objects.get(slug=tag_name)
                        event.tags.add(tag)
                    except EventTag.DoesNotExist:
                        pass
                
                self.stdout.write(f'Created event: {event.title}')
            else:
                self.stdout.write(f'Event already exists: {event.title}')

        self.stdout.write(self.style.SUCCESS('Sample events created successfully!'))
