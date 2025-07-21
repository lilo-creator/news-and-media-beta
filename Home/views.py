from django.shortcuts import render, get_object_or_404
from .models import LandingFeature
from News.models import Article, Category

# Create your views here.
def home(request):
    """View function for the home page."""
    # Get all active landing features by section
    news_features = LandingFeature.objects.filter(is_active=True, section='news')
    sports_features = LandingFeature.objects.filter(is_active=True, section='sports')
    events_features = LandingFeature.objects.filter(is_active=True, section='events')
    
    # Get featured news articles
    featured_news = Article.objects.filter(status='published', featured=True).order_by('-publish_date')[:3]
    
    # Get all news categories
    categories = Category.objects.all()
    
    context = {
        'news_features': news_features,
        'sports_features': sports_features,
        'events_features': events_features,
        'featured_news': featured_news,
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