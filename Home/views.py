from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import LandingFeature
from News.models import Article, Category
from Events.models import Event

# Create your views here.
def home(request):
    """View function for the home page."""
    # Get all active landing features by section
    news_features = LandingFeature.objects.filter(is_active=True, section='news')
    sports_features = LandingFeature.objects.filter(is_active=True, section='sports')
    events_features = LandingFeature.objects.filter(is_active=True, section='events')
    
    # Get main story (latest featured article)
    main_story = Article.objects.filter(
        status='published',
        featured=True
    ).order_by('-publish_date').first()
    
    # Get trending stories (most viewed in the last 7 days)
    trending_stories = Article.objects.filter(
        status='published',
        publish_date__gte=timezone.now() - timezone.timedelta(days=7)
    ).order_by('-view_count')[:3]
    
    # Get featured news articles for breaking news ticker
    featured_news = Article.objects.filter(
        status='published',
        featured=True
    ).order_by('-publish_date')[:3]
    
    # Get featured stories for the grid
    featured_stories = Article.objects.filter(
        status='published',
        featured=True
    ).exclude(id=main_story.id if main_story else None).order_by('-publish_date')[:6]
    
    # If not enough featured stories, get regular published articles
    if featured_stories.count() < 6:
        regular_stories = Article.objects.filter(
            status='published'
        ).exclude(
            id__in=[story.id for story in featured_stories]
        ).exclude(
            id=main_story.id if main_story else None
        ).order_by('-publish_date')[:6-featured_stories.count()]
        
        # Combine featured and regular stories
        featured_stories = list(featured_stories) + list(regular_stories)
    
    # Create context dictionary for template rendering
    context = {
        'main_story': main_story,
        'trending_stories': trending_stories,
        'featured_news': featured_news,
        'featured_stories': featured_stories,
    }
    
    return render(request, 'Home/home.html', context)
    
    # Get upcoming events (events that haven't started yet)
    now = timezone.now()
    upcoming_events = Event.objects.filter(
        is_active=True,
        date__gte=now.date()
    ).order_by('date', 'start_time')[:6]  # Show 6 upcoming events
    
    # Get all news categories
    categories = Category.objects.all()
    
    context = {
        'news_features': news_features,
        'sports_features': sports_features,
        'events_features': events_features,
        'featured_news': all_news,  # Now includes both featured and regular articles
        'upcoming_events': upcoming_events,
        'categories': categories,
    }
    
    return render(request, 'Home/home.html', context)

from django.shortcuts import render, get_object_or_404

def feature_detail(request, feature_id):
    """View function for the feature detail page."""
    feature = get_object_or_404(LandingFeature, id=feature_id)
    
    context = {
        'feature': feature
    }
    
    return render(request, 'Home/feature_detail.html', context)