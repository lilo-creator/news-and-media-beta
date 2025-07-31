from django.shortcuts import render
from News.views import get_dummy_articles
from Sports.views import get_dummy_sports
from Events.views import get_dummy_events
import datetime

def get_dummy_home_data():
    """Return dummy data for home page."""
    return {
        'main_story': {
            'title': 'Historic Peace Agreement Signed in Middle East',
            'slug': 'middle-east-peace-agreement',
            'excerpt': 'After decades of conflict, regional powers have reached a comprehensive peace accord that addresses territorial disputes, security concerns, and economic cooperation frameworks.',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?q=80&w=1435&auto=format&fit=crop',
            'publish_date': '2025-07-14',
            'view_count': 3245,
            'author': {'get_full_name': 'Omar Hassan'},
            'category': {'name': 'Politics', 'slug': 'politics'},
            'featured': True,
        },
        'trending_stories': [
            {
                'title': 'International Space Mission Successfully Lands on Mars',
                'slug': 'mars-landing-mission',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?q=80&w=1474&auto=format&fit=crop',
                'excerpt': 'The multinational spacecraft has touched down safely on the Martian surface, beginning a new chapter in interplanetary exploration.',
                'category': {'name': 'Science', 'slug': 'science'},
                'publish_date': '2025-07-16',
                'view_count': 2145,
                'author': {'get_full_name': 'Priya Sharma'},
            },
            {
                'title': 'Breakthrough in Quantum Computing Achieves New Milestone',
                'slug': 'quantum-computing-milestone',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=1470&auto=format&fit=crop',
                'excerpt': 'Scientists have successfully maintained quantum coherence for a record duration, bringing practical quantum computing applications significantly closer to reality.',
                'category': {'name': 'Technology', 'slug': 'technology'},
                'publish_date': '2025-07-15',
                'view_count': 1836,
                'author': {'get_full_name': 'Michael Chen'},
            },
            {
                'title': 'Major Security Vulnerability Discovered in Popular Software',
                'slug': 'security-vulnerability-software',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=1470&auto=format&fit=crop',
                'excerpt': 'Cybersecurity experts urge immediate updates as critical flaw affects millions of users worldwide.',
                'category': {'name': 'Technology', 'slug': 'technology'},
                'publish_date': '2025-07-18',
                'view_count': 1125,
                'author': {'get_full_name': 'Sarah Johnson'},
            },
        ],
        'breaking_news': [
            'Historic Peace Agreement Signed in Middle East after decades of conflict',
            'New AI Technology Breakthrough Promises Revolutionary Changes in healthcare and education',
            'Global Summit on Climate Change Reaches Landmark Agreement with ambitious targets',
            'International Space Mission Successfully Lands on Mars, beginning a new chapter in exploration'
        ],
        'featured_events': [
            {
                'title': 'Tech Summit 2025',
                'slug': 'tech-summit-2025',
                'banner_image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?q=80&w=2070&auto=format&fit=crop',
                'date': datetime.date(2025, 8, 15),
                'venue_name': 'Tech Convention Center',
                'tags': [{'name': 'Technology'}, {'name': 'AI'}],
            },
            {
                'title': 'Summer Music Festival',
                'slug': 'summer-music-festival-2025',
                'banner_image_url': 'https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?q=80&w=2070&auto=format&fit=crop',
                'date': datetime.date(2025, 8, 20),
                'venue_name': 'City Park Amphitheater',
                'tags': [{'name': 'Music'}, {'name': 'Entertainment'}],
            }
        ],
        'featured_sports': [
            {
                'name': 'Football',
                'headline': 'Manchester City clinched a dramatic win over Arsenal in a thrilling Premier League encounter',
                'image_url': 'https://resources.premierleague.pulselive.com/photo-resources/2025/07/17/a3bb7df8-7c88-4b27-8cbe-2394dfdcbfc8/Haaland-Maguire.jpg?width=1440&height=810',
                'sport': 'Football',
            },
            {
                'name': 'Basketball',
                'headline': 'NBA 2K26 All-Summer League teams announced',
                'image_url': 'https://cdn.nba.com/manage/2025/07/16x9First-Team-1-1568x882.png',
                'sport': 'Basketball',
            }
        ]
    }

# Create your views here.
def home(request):
    """View function for the home page."""
    # Get dummy data
    home_data = get_dummy_home_data()
    news_articles = get_dummy_articles()
    events = get_dummy_events()
    sports = get_dummy_sports()
    
    # Create context dictionary for template rendering
    context = {
        'main_story': home_data['main_story'],
        'trending_stories': home_data['trending_stories'],
        'breaking_news': home_data['breaking_news'],
        'featured_events': home_data['featured_events'],
        'featured_sports': home_data['featured_sports'],
        'latest_news': news_articles[:6],
        'categories': [
            {'name': 'Technology', 'slug': 'technology'},
            {'name': 'Politics', 'slug': 'politics'},
            {'name': 'Health', 'slug': 'health'},
            {'name': 'Business', 'slug': 'business'},
            {'name': 'Entertainment', 'slug': 'entertainment'},
            {'name': 'Science', 'slug': 'science'},
            {'name': 'Sports', 'slug': 'sports'},
        ]
    }
    
    return render(request, 'Home/home_new.html', context)

def feature_detail(request, feature_id):
    """View function for the feature detail page."""
    # Dummy feature data
    feature = {
        'id': feature_id,
        'title': 'Featured Content',
        'description': 'This is a featured content item with detailed information.',
        'image_url': 'https://via.placeholder.com/800x400',
        'content': '<p>This is the detailed content of the feature. It includes rich text formatting and possibly embedded media.</p>',
    }
    
    context = {
        'feature': feature
    }
    
    return render(request, 'Home/feature_detail.html', context)