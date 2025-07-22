#!/usr/bin/env python
"""
Script to add sample events with banner images for testing the home page display.
"""

import os
import sys
import django
from datetime import date, time, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from Events.models import Event, EventHost, EventTag

def create_sample_events_with_images():
    print("Creating sample events with images...")
    
    # Create or get a sample host
    host, created = EventHost.objects.get_or_create(
        name="City Events Organization",
        defaults={
            'contact_email': 'info@cityevents.com',
            'description': 'Premier event organizer in the city'
        }
    )
    
    # Create or get some tags
    tech_tag, _ = EventTag.objects.get_or_create(
        name="Technology", 
        defaults={'slug': 'technology', 'color': '#007bff'}
    )
    music_tag, _ = EventTag.objects.get_or_create(
        name="Music", 
        defaults={'slug': 'music', 'color': '#28a745'}
    )
    business_tag, _ = EventTag.objects.get_or_create(
        name="Business", 
        defaults={'slug': 'business', 'color': '#ffc107'}
    )
    
    # Sample events data with banner image URLs
    events_data = [
        {
            'title': 'Tech Innovation Summit 2025',
            'slug': 'tech-innovation-summit-2025',
            'description': 'Join industry leaders for cutting-edge technology discussions, networking, and innovation showcases. Discover the latest trends in AI, blockchain, and emerging technologies.',
            'date': date.today() + timedelta(days=15),
            'start_time': time(9, 0),
            'end_time': time(17, 0),
            'venue_name': 'Convention Center',
            'venue_address': '123 Tech Street, Innovation District',
            'banner_image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&h=400&fit=crop',
            'ticket_price': '$150 - $300',
            'tags': [tech_tag],
        },
        {
            'title': 'Summer Music Festival',
            'slug': 'summer-music-festival-2025',
            'description': 'A spectacular outdoor music festival featuring local and international artists across multiple genres. Food trucks, art installations, and family-friendly activities.',
            'date': date.today() + timedelta(days=25),
            'start_time': time(14, 0),
            'end_time': time(23, 0),
            'venue_name': 'Central Park Amphitheater',
            'venue_address': '456 Music Avenue, Downtown',
            'banner_image_url': 'https://images.unsplash.com/photo-1459749411175-04bf5292ceea?w=600&h=400&fit=crop',
            'ticket_price': '$75 - $200',
            'tags': [music_tag],
        },
        {
            'title': 'Business Leadership Conference',
            'slug': 'business-leadership-conference-2025',
            'description': 'Empower your leadership skills with renowned speakers, interactive workshops, and networking opportunities with industry executives and entrepreneurs.',
            'date': date.today() + timedelta(days=8),
            'start_time': time(8, 30),
            'end_time': time(18, 0),
            'venue_name': 'Grand Hotel Ballroom',
            'venue_address': '789 Business Blvd, Corporate District',
            'banner_image_url': 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=600&h=400&fit=crop',
            'ticket_price': '$200 - $500',
            'tags': [business_tag],
        },
        {
            'title': 'Community Food & Culture Fair',
            'slug': 'community-food-culture-fair-2025',
            'description': 'Celebrate diversity with authentic cuisines from around the world, cultural performances, cooking demonstrations, and artisan crafts.',
            'date': date.today() + timedelta(days=12),
            'start_time': time(11, 0),
            'end_time': time(20, 0),
            'venue_name': 'Riverside Park',
            'venue_address': '321 River Road, Cultural Quarter',
            'banner_image_url': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop',
            'ticket_price': 'Free Entry',
            'tags': [],
        },
        {
            'title': 'Digital Marketing Workshop',
            'slug': 'digital-marketing-workshop-2025',
            'description': 'Hands-on workshop covering social media strategy, content creation, SEO optimization, and digital advertising for small businesses and entrepreneurs.',
            'date': date.today() + timedelta(days=6),
            'start_time': time(10, 0),
            'end_time': time(16, 0),
            'venue_name': 'Learning Hub',
            'venue_address': '567 Education Street, Business Park',
            'banner_image_url': 'https://images.unsplash.com/photo-1553028826-f4804151e19b?w=600&h=400&fit=crop',
            'ticket_price': '$120',
            'tags': [tech_tag, business_tag],
        },
        {
            'title': 'Art & Wine Evening',
            'slug': 'art-wine-evening-2025',
            'description': 'An elegant evening showcasing local artists, wine tasting from regional vineyards, and live acoustic performances in an intimate gallery setting.',
            'date': date.today() + timedelta(days=20),
            'start_time': time(18, 0),
            'end_time': time(22, 0),
            'venue_name': 'Modern Art Gallery',
            'venue_address': '890 Gallery Lane, Arts District',
            'banner_image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=600&h=400&fit=crop',
            'ticket_price': '$85',
            'tags': [],
        },
    ]
    
    # Create events
    created_count = 0
    for event_data in events_data:
        tags = event_data.pop('tags', [])
        
        event, created = Event.objects.get_or_create(
            slug=event_data['slug'],
            defaults={
                **event_data,
                'host': host,
                'is_active': True,
                'is_featured': True
            }
        )
        
        if created:
            # Add tags
            for tag in tags:
                event.tags.add(tag)
            
            created_count += 1
            print(f"✓ Created: {event.title}")
        else:
            print(f"- Already exists: {event.title}")
    
    print(f"\nCompleted! Created {created_count} new events with banner images.")
    print("These events will now display with images on the home page.")

if __name__ == "__main__":
    create_sample_events_with_images()
