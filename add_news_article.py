import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from News.models import Article, Category
from django.contrib.auth.models import User
from django.utils.text import slugify

# Ensure at least one user exists
username = 'newsbot'
user, created = User.objects.get_or_create(username=username, defaults={
    'email': 'newsbot@example.com',
    'is_staff': True,
    'is_superuser': False
})
if created:
    user.set_password('newsbotpassword')
    user.save()

# Define categories
categories = [
    {'name': 'Politics', 'slug': 'politics'},
    {'name': 'Entertainment', 'slug': 'entertainment'},
    {'name': 'Tech', 'slug': 'tech'},
]
category_objs = {}
for cat in categories:
    obj, _ = Category.objects.get_or_create(name=cat['name'], slug=cat['slug'])
    category_objs[cat['slug']] = obj

# News articles with images and balanced categories
news_articles = [
    {
        'title': 'Kenya Parliament Passes Landmark Bill',
        'excerpt': 'Kenya’s parliament has passed a landmark bill aimed at electoral reforms ahead of the 2027 elections.',
        'content': 'The new bill introduces sweeping changes to the electoral process, including digital voting and enhanced transparency. Lawmakers say the reforms will strengthen democracy and public trust.',
        'category': 'politics',
        'image': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80',
    },
    {
        'title': 'Hollywood Blockbuster Breaks Box Office Records',
        'excerpt': 'The latest Hollywood blockbuster has shattered box office records, grossing over $1 billion worldwide.',
        'content': 'Critics and fans alike are praising the film for its stunning visuals and compelling story. The movie’s director says a sequel is already in the works.',
        'category': 'entertainment',
        'image': 'https://images.unsplash.com/photo-1517602302552-471fe67acf66?auto=format&fit=crop&w=800&q=80',
    },
    {
        'title': 'Breakthrough in Quantum Computing Announced',
        'excerpt': 'A major breakthrough in quantum computing could revolutionize technology and cybersecurity.',
        'content': 'Researchers at a leading tech company have developed a new quantum processor that can solve complex problems in seconds. Experts say this could lead to advances in medicine, finance, and artificial intelligence.',
        'category': 'tech',
        'image': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=800&q=80',
    },
]

for news in news_articles:
    slug = slugify(news['title'])
    article, created = Article.objects.get_or_create(
        title=news['title'],
        slug=slug,
        author=user,
        category=category_objs[news['category']],
        defaults={
            'excerpt': news['excerpt'],
            'content': news['content'],
            'status': 'published',
            'featured': False
        }
    )
    if created:
        # Set the featured_image field to the image URL (if using URLField or handle download if using ImageField)
        article.featured_image = news['image']
        article.save()
        print(f"News article created: {article.title}")
    else:
        print(f"News article already exists: {article.title}")
