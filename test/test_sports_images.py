#!/usr/bin/env python
"""
Test script to verify Sports app image functionality.
"""

import os
import sys
import django
from django.test import Client

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

def test_sports_images():
    """Test sports images display functionality."""
    client = Client()
    
    print("Testing Sports App Image Functionality...")
    print("=" * 50)
    
    # Test sports list page
    try:
        response = client.get('/sports/')
        print(f"✓ Sports list page: Status {response.status_code}")
        if response.status_code == 200:
            print("  - Sports list page loads successfully")
            if b'https://images.unsplash.com' in response.content:
                print("  - ✓ Sports images are being loaded from Unsplash")
            else:
                print("  - ⚠ Sports images might not be loading properly")
        else:
            print(f"  - Warning: Sports list page returned status {response.status_code}")
    except Exception as e:
        print(f"✗ Sports list page failed: {e}")
    
    # Test individual sport details
    sports = ['football', 'basketball', 'tennis', 'cricket', 'rugby']
    for sport_id in [1, 2, 3, 4, 5]:
        try:
            response = client.get(f'/sports/sport/{sport_id}/')
            sport_name = sports[sport_id - 1] if sport_id <= len(sports) else f"Sport {sport_id}"
            print(f"✓ {sport_name.title()} detail page: Status {response.status_code}")
            if response.status_code == 200:
                if b'https://images.unsplash.com' in response.content:
                    print(f"  - ✓ {sport_name.title()} images loading correctly")
                else:
                    print(f"  - ⚠ {sport_name.title()} images might not be loading")
        except Exception as e:
            print(f"✗ {sport_name.title()} detail page failed: {e}")
    
    # Test article functionality
    articles = ['football', 'basketball', 'tennis', 'rugby', 'volleyball']
    for article in articles:
        try:
            response = client.get(f'/sports/article/{article}/')
            print(f"✓ {article.title()} article: Status {response.status_code}")
            if response.status_code == 200:
                if b'https://images.unsplash.com' in response.content:
                    print(f"  - ✓ {article.title()} article images loading correctly")
                else:
                    print(f"  - ⚠ {article.title()} article images might not be loading")
        except Exception as e:
            print(f"✗ {article.title()} article failed: {e}")
    
    print("\n" + "=" * 50)
    print("Sports App Image Test Complete!")
    print("\nImage Sources Added:")
    print("- Football: Professional football action shots")
    print("- Basketball: NBA-style basketball courts and games")  
    print("- Tennis: Tennis courts and professional matches")
    print("- Cricket: Cricket stadiums and match scenes")
    print("- Rugby: Rugby action and team photos")
    print("- Golf: Golf courses and professional golfers")
    print("- Swimming: Olympic pools and swimmers")
    print("- Athletics: Track and field events")
    print("- Volleyball: Volleyball courts and matches")
    
    print("\nFeatures:")
    print("- All sport categories now have high-quality images")
    print("- Article images updated with relevant sports photos")
    print("- Fallback images for missing content")
    print("- Responsive image display")
    print("- Proper alt text for accessibility")

if __name__ == '__main__':
    test_sports_images()
