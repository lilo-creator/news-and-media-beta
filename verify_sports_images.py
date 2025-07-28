#!/usr/bin/env python
"""
Simple script to verify Sports app images are working properly
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

# Now import Django modules
from Sports.views import get_dummy_sports

def test_sports_images():
    """Test that all sports have valid image URLs"""
    print("🏆 Testing Sports App Images...")
    print("=" * 50)
    
    sports = get_dummy_sports()
    
    total_sports = len(sports)
    sports_with_images = 0
    
    for sport in sports:
        name = sport.get('name', 'Unknown')
        image_data = sport.get('image')
        
        if image_data:
            if isinstance(image_data, dict):
                url = image_data.get('url', '')
            else:
                url = str(image_data)
            
            if url and url != 'None' and 'unsplash.com' in url:
                print(f"✅ {name}: {url[:60]}...")
                sports_with_images += 1
            else:
                print(f"❌ {name}: Invalid or missing image URL")
        else:
            print(f"❌ {name}: No image data found")
    
    print("=" * 50)
    print(f"📊 Results: {sports_with_images}/{total_sports} sports have valid images")
    
    if sports_with_images == total_sports:
        print("🎉 SUCCESS: All sports have valid image URLs!")
        return True
    else:
        print("⚠️  WARNING: Some sports are missing valid images")
        return False

if __name__ == '__main__':
    try:
        success = test_sports_images()
        
        print("\n🔗 Test the Sports page at: http://127.0.0.1:8000/sports/")
        
        if success:
            print("\n✨ All sports images should now be displaying properly!")
        else:
            print("\n🔧 Some images may need fixing")
            
    except Exception as e:
        print(f"❌ Error running test: {e}")
        sys.exit(1)
