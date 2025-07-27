#!/usr/bin/env python
"""
Update existing articles with featured image URLs using local static images
"""
import os
import django
import sys
from django.core.files.images import ImageFile

# Setup Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from News.models import Article
from django.conf import settings

def add_images():
    # Use available local images
    static_images = [
        'static/basketball_lakers_bulls.jpg', 
        'static/football_mancity_arsenal.jpg'
    ]
    
    # Check if these files exist
    available_images = []
    for img_path in static_images:
        full_path = os.path.join(settings.BASE_DIR, img_path)
        if os.path.exists(full_path):
            available_images.append(full_path)
            print(f"Found image: {full_path}")
    
    if not available_images:
        print("No local images found to use! Using dummy values.")
        # We'll just clean up the content without setting images
        for article in Article.objects.all():
            if 'IMAGE_URL:' in article.content:
                # Remove the IMAGE_URL line from content
                lines = article.content.split("\n\n", 1)
                if lines[0].startswith('IMAGE_URL:'):
                    article.content = lines[1] if len(lines) > 1 else ""
                    article.save()
                    print(f"Cleaned up content for: {article.title}")
        return
    
    # Process all articles
    for article in Article.objects.all():
        # Skip if article already has an image
        if article.featured_image:
            print(f"Article already has image: {article.title}")
            continue
            
        # Clean up any old IMAGE_URL references in the content
        if 'IMAGE_URL:' in article.content:
            lines = article.content.split("\n\n", 1)
            if lines[0].startswith('IMAGE_URL:'):
                article.content = lines[1] if len(lines) > 1 else ""
                article.save()
        
        # Choose an image (alternate between available images)
        img_path = available_images[article.id % len(available_images)]
        
        try:
            # Save the image to the featured_image field
            with open(img_path, 'rb') as img_file:
                image_name = f"{article.slug}_featured.jpg"
                article.featured_image.save(image_name, ImageFile(img_file), save=True)
                print(f"Added image to: {article.title}")
        except Exception as e:
            print(f"Error adding image for {article.title}: {str(e)}")
    
    print(f"Total articles: {Article.objects.count()}")

if __name__ == '__main__':
    add_images()

if __name__ == '__main__':
    add_images()
