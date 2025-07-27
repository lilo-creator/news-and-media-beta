#!/usr/bin/env python
"""
Simple script to add sample news articles
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from News.models import Category, Tag, Article
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Get or create admin user
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'first_name': 'Admin',
        'last_name': 'User',
        'is_staff': True,
        'is_superuser': True
    }
)

# Create categories
categories = [
    {'name': 'Breaking News', 'slug': 'breaking-news'},
    {'name': 'Technology', 'slug': 'technology'},
    {'name': 'Politics', 'slug': 'politics'},
    {'name': 'Entertainment', 'slug': 'entertainment'},
    {'name': 'Health', 'slug': 'health'},
    {'name': 'Business', 'slug': 'business'}
]

for cat in categories:
    Category.objects.get_or_create(
        slug=cat['slug'],
        defaults={'name': cat['name'], 'description': f'Latest {cat["name"]} news'}
    )

# Create sample articles
tech_cat = Category.objects.get(slug='technology')
breaking_cat = Category.objects.get(slug='breaking-news')
politics_cat = Category.objects.get(slug='politics')
entertainment_cat = Category.objects.get(slug='entertainment')

articles = [
    {
        'title': 'Revolutionary AI Technology Transforms Healthcare',
        'category': tech_cat,
        'excerpt': 'New AI system shows 85% accuracy in early disease detection',
        'content': '<p>A groundbreaking AI system is revolutionizing healthcare...</p>',
        'featured': True
    },
    {
        'title': 'Global Climate Summit Reaches Historic Agreement',
        'category': breaking_cat,
        'excerpt': 'World leaders commit to net-zero emissions by 2040',
        'content': '<p>Historic climate agreement reached at global summit...</p>',
        'featured': True
    },
    {
        'title': 'Major Election Updates: Record Voter Turnout',
        'category': politics_cat,
        'excerpt': 'Highest voter participation expected in decades',
        'content': '<p>Political analysts predict record-breaking turnout...</p>',
        'featured': False
    },
    {
        'title': 'VR Revolution in Entertainment Industry',
        'category': entertainment_cat,
        'excerpt': 'Studios invest $500M in virtual reality experiences',
        'content': '<p>Entertainment industry embraces VR technology...</p>',
        'featured': False
    }
]

for i, article_data in enumerate(articles):
    Article.objects.get_or_create(
        slug=slugify(article_data['title']),
        defaults={
            'title': article_data['title'],
            'author': admin_user,
            'category': article_data['category'],
            'excerpt': article_data['excerpt'],
            'content': article_data['content'],
            'status': 'published',
            'featured': article_data['featured'],
            'publish_date': timezone.now() - timedelta(days=i),
            'view_count': (i + 1) * 100
        }
    )

print("Sample news articles created successfully!")
