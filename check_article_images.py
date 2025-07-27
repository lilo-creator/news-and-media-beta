import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from News.models import Article
from django.conf import settings

def check_article_images():
    print("Checking article images...")
    articles = Article.objects.all()
    print(f"Found {articles.count()} articles")
    
    for article in articles:
        print(f"\nArticle ID: {article.id}")
        print(f"Title: {article.title}")
        print(f"Featured Image Path: {article.featured_image}")
        
        if article.featured_image and hasattr(article.featured_image, 'url'):
            full_path = f"{settings.MEDIA_ROOT}/{article.featured_image}"
            url = article.featured_image.url
            physical_exists = os.path.exists(full_path)
            
            print(f"Image URL: {url}")
            print(f"Physical path: {full_path}")
            print(f"File exists: {physical_exists}")
            
            try:
                method_url = article.get_featured_image_url()
                print(f"URL from get_featured_image_url(): {method_url}")
            except Exception as e:
                print(f"Error getting URL from method: {str(e)}")
        else:
            print("No featured image set or image attribute error")
            print(f"URL from get_featured_image_url(): {article.get_featured_image_url()}")

if __name__ == "__main__":
    check_article_images()
