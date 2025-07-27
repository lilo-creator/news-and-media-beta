#!/usr/bin/env python
"""
Script to populate the News app with dummy data including categories, tags, and articles.
"""

import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.text import slugify

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

# Now import Django models
from News.models import Category, Tag, Article
from django.contrib.auth.models import User

def create_dummy_data():
    """Create dummy news data"""
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@newsandmedia.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("✅ Created admin user")
    else:
        admin_user = User.objects.get(username='admin')
        print("✅ Using existing admin user")

    # Create additional users
    users_data = [
        {'username': 'john_reporter', 'first_name': 'John', 'last_name': 'Smith', 'email': 'john@newsandmedia.com'},
        {'username': 'sarah_editor', 'first_name': 'Sarah', 'last_name': 'Johnson', 'email': 'sarah@newsandmedia.com'},
        {'username': 'mike_writer', 'first_name': 'Mike', 'last_name': 'Brown', 'email': 'mike@newsandmedia.com'},
    ]
    
    created_users = [admin_user]
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': user_data['email']
            }
        )
        created_users.append(user)
        if created:
            print(f"✅ Created user: {user.get_full_name()}")
        else:
            print(f"✅ Using existing user: {user.get_full_name()}")

    # Create categories
    categories_data = [
        {
            'name': 'Breaking News',
            'slug': 'breaking-news',
            'description': 'Latest breaking news and urgent updates from around the world.'
        },
        {
            'name': 'Politics',
            'slug': 'politics',
            'description': 'Political news, government updates, and policy discussions.'
        },
        {
            'name': 'Technology',
            'slug': 'technology',
            'description': 'Latest in tech innovations, gadgets, and digital trends.'
        },
        {
            'name': 'Entertainment',
            'slug': 'entertainment',
            'description': 'Celebrity news, movies, music, and entertainment industry updates.'
        },
        {
            'name': 'Health',
            'slug': 'health',
            'description': 'Health news, medical breakthroughs, and wellness tips.'
        },
        {
            'name': 'Business',
            'slug': 'business',
            'description': 'Business news, market updates, and economic analysis.'
        }
    ]

    created_categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={
                'name': cat_data['name'],
                'description': cat_data['description']
            }
        )
        created_categories.append(category)
        if created:
            print(f"✅ Created category: {category.name}")
        else:
            print(f"✅ Using existing category: {category.name}")

    # Create tags
    tags_data = [
        'trending', 'urgent', 'exclusive', 'investigation', 'interview',
        'analysis', 'opinion', 'feature', 'breaking', 'update',
        'technology', 'innovation', 'startup', 'ai', 'blockchain',
        'politics', 'election', 'policy', 'government', 'international'
    ]

    created_tags = []
    for tag_name in tags_data:
        tag, created = Tag.objects.get_or_create(
            slug=slugify(tag_name),
            defaults={'name': tag_name}
        )
        created_tags.append(tag)
        if created:
            print(f"✅ Created tag: {tag.name}")

    # Create articles
    articles_data = [
        {
            'title': 'Revolutionary AI Technology Transforms Healthcare Industry',
            'category': 'technology',
            'excerpt': 'A groundbreaking AI system is revolutionizing patient care and diagnosis accuracy across major hospitals worldwide.',
            'content': '''
            <p>The healthcare industry is experiencing a seismic shift with the introduction of advanced artificial intelligence systems that are transforming patient care and medical diagnostics. This revolutionary technology has been implemented in over 200 hospitals worldwide, showing remarkable improvements in diagnostic accuracy and treatment outcomes.</p>

            <p>The AI system, developed by leading technology companies in collaboration with medical professionals, utilizes machine learning algorithms to analyze patient data, medical images, and laboratory results with unprecedented precision. Early trials have shown a 35% improvement in diagnostic accuracy compared to traditional methods.</p>

            <p>"This technology represents a paradigm shift in how we approach healthcare," said Dr. Emily Rodriguez, Chief Medical Officer at Metropolitan General Hospital. "The AI's ability to process vast amounts of medical data and identify patterns that might be missed by human analysis is truly remarkable."</p>

            <p>The implementation has not only improved patient outcomes but also reduced healthcare costs significantly. Hospitals report a 25% reduction in unnecessary procedures and a 40% decrease in diagnostic wait times.</p>

            <p>Looking ahead, researchers are optimistic about the potential for even more advanced applications, including personalized treatment plans and predictive health analytics that could prevent diseases before they manifest.</p>
            ''',
            'tags': ['technology', 'ai', 'innovation', 'trending'],
            'featured': True,
            'status': 'published'
        },
        {
            'title': 'Global Climate Summit Reaches Historic Agreement on Carbon Reduction',
            'category': 'breaking-news',
            'excerpt': 'World leaders unite in unprecedented commitment to achieve net-zero emissions by 2040, setting new global environmental standards.',
            'content': '''
            <p>In a historic moment for environmental action, world leaders at the Global Climate Summit have reached an unprecedented agreement to achieve net-zero carbon emissions by 2040, moving the deadline forward by a full decade from previous commitments.</p>

            <p>The agreement, signed by representatives from 195 countries, includes binding commitments to renewable energy investments, carbon capture technologies, and sustainable development practices. This marks the most ambitious climate action plan in history.</p>

            <p>"Today, we've chosen the future of our planet over short-term economic interests," declared UN Climate Chief Maria Santos during the closing ceremony. "This agreement represents humanity's commitment to leaving a habitable world for future generations."</p>

            <p>Key provisions of the agreement include:
            • $2 trillion in renewable energy investments over the next decade
            • Mandatory carbon capture implementation for major industries
            • Support funds for developing nations to transition to clean energy
            • Strict penalties for countries failing to meet emission targets</p>

            <p>Environmental scientists and activists worldwide have praised the agreement, calling it a "turning point" in the fight against climate change. The implementation timeline begins immediately, with quarterly progress reports required from all participating nations.</p>
            ''',
            'tags': ['breaking', 'urgent', 'international', 'trending'],
            'featured': True,
            'status': 'published'
        },
        {
            'title': 'Major Election Updates: Record Voter Turnout Expected',
            'category': 'politics',
            'excerpt': 'Political analysts predict highest voter participation in decades as citizens gear up for crucial elections nationwide.',
            'content': '''
            <p>Political analysts across the country are predicting record-breaking voter turnout for the upcoming elections, with early voting numbers already surpassing previous records by 40%. This surge in civic engagement reflects the high stakes and intense public interest in this election cycle.</p>

            <p>Early voting centers report long lines and enthusiastic participation from voters of all demographics. "We've never seen anything like this," said Election Commissioner Janet Williams. "The level of engagement is extraordinary, and it's clear that citizens understand the importance of their voice in this democracy."</p>

            <p>Key factors driving the increased participation include:
            • Expanded mail-in voting options
            • Extended early voting periods
            • Increased voter education campaigns
            • Heightened public awareness of key issues</p>

            <p>Candidates from all parties have noted the energy and enthusiasm among voters. Campaign organizers report unprecedented volunteer sign-ups and grassroots fundraising efforts.</p>

            <p>Election officials are working around the clock to ensure smooth operations, with additional polling stations opened and extended hours implemented to accommodate the expected crowds on election day.</p>
            ''',
            'tags': ['politics', 'election', 'trending', 'update'],
            'featured': False,
            'status': 'published'
        },
        {
            'title': 'Entertainment Industry Embraces Virtual Reality Experiences',
            'category': 'entertainment',
            'excerpt': 'Major studios announce groundbreaking VR projects that promise to revolutionize how audiences experience movies and concerts.',
            'content': '''
            <p>The entertainment industry is on the brink of a revolutionary transformation as major studios and production companies announce ambitious virtual reality projects that will fundamentally change how audiences experience movies, concerts, and live performances.</p>

            <p>Leading the charge, several Hollywood studios have invested over $500 million in VR technology development, creating immersive experiences that allow viewers to step inside their favorite films and interact with characters in unprecedented ways.</p>

            <p>"We're not just watching entertainment anymore; we're living it," explained VR Director Lisa Chen. "These new technologies allow audiences to become active participants in the storytelling process, creating personalized and unforgettable experiences."</p>

            <p>The music industry is equally excited about VR possibilities, with major artists planning virtual concerts that can accommodate millions of viewers simultaneously. These events will feature interactive elements, allowing fans to influence lighting, camera angles, and even song selections in real-time.</p>

            <p>Early beta tests have received overwhelmingly positive feedback, with 95% of participants rating their VR entertainment experiences as "transformative" or "life-changing." The technology is expected to be commercially available by next year.</p>
            ''',
            'tags': ['entertainment', 'technology', 'innovation', 'feature'],
            'featured': False,
            'status': 'published'
        },
        {
            'title': 'Breakthrough Medical Research Offers Hope for Rare Diseases',
            'category': 'health',
            'excerpt': 'Scientists develop innovative gene therapy treatments showing remarkable success rates in treating previously incurable conditions.',
            'content': '''
            <p>Medical researchers have achieved a significant breakthrough in gene therapy, developing treatments that show remarkable success rates in addressing rare diseases that were previously considered incurable. The research, conducted across multiple international medical centers, represents a new frontier in personalized medicine.</p>

            <p>The innovative therapy technique, known as CRISPR-Enhanced Gene Correction (CEGC), has shown success rates exceeding 85% in early clinical trials involving patients with rare genetic disorders. This represents a quantum leap forward from previous treatment options.</p>

            <p>Dr. Robert Kim, lead researcher at the International Gene Therapy Institute, explains: "What we're seeing is not just treatment, but actual correction of genetic abnormalities at the cellular level. Patients who had no hope for improvement are now experiencing significant recovery."</p>

            <p>The treatment process involves:
            • Precise genetic mapping of the patient's condition
            • Customized gene therapy tailored to individual genetic profiles
            • Minimally invasive delivery systems
            • Ongoing monitoring and adjustment protocols</p>

            <p>Families affected by rare diseases are expressing unprecedented hope and gratitude. The therapy is expected to receive fast-track approval from regulatory agencies, potentially becoming available to patients within 18 months.</p>
            ''',
            'tags': ['health', 'innovation', 'exclusive', 'trending'],
            'featured': False,
            'status': 'published'
        },
        {
            'title': 'Stock Markets Reach All-Time Highs Amid Economic Optimism',
            'category': 'business',
            'excerpt': 'Major indices surge to record levels as investor confidence grows following positive economic indicators and corporate earnings.',
            'content': '''
            <p>Global stock markets have reached unprecedented heights this week, with major indices setting new all-time records amid growing investor confidence and positive economic indicators. The surge reflects optimism about economic recovery and strong corporate earnings across multiple sectors.</p>

            <p>The technology sector led the rally, with major tech companies reporting quarterly earnings that exceeded analyst expectations by an average of 25%. This performance has been driven by increased demand for digital services and continued innovation in emerging technologies.</p>

            <p>Market analyst Sarah Thompson notes, "We're seeing a perfect storm of positive factors: strong corporate earnings, low unemployment rates, increasing consumer confidence, and continued technological advancement. These elements are creating an incredibly bullish market environment."</p>

            <p>Key market highlights include:
            • S&P 500 up 3.2% for the week
            • Technology sector leading with 5.1% gains
            • International markets following suit with strong performance
            • Record trading volumes indicating high investor participation</p>

            <p>Economic experts remain cautiously optimistic, noting that while current trends are positive, investors should maintain balanced portfolios and consider long-term strategies. The Federal Reserve has indicated its commitment to supporting continued economic growth while monitoring inflation indicators.</p>
            ''',
            'tags': ['business', 'analysis', 'trending', 'update'],
            'featured': False,
            'status': 'published'
        },
        {
            'title': 'Space Exploration Milestone: Private Mission Successfully Reaches Mars',
            'category': 'technology',
            'excerpt': 'Historic achievement as private aerospace company completes first commercially-funded mission to Mars, opening new possibilities for space exploration.',
            'content': '''
            <p>In a historic achievement that marks a new era in space exploration, a private aerospace company has successfully completed the first commercially-funded mission to Mars. The mission, which launched eight months ago, has transmitted stunning images and valuable scientific data back to Earth.</p>

            <p>The spacecraft, equipped with advanced scientific instruments and communication systems, landed safely in the Martian northern hemisphere and has begun conducting experiments designed to search for signs of past or present life on the Red Planet.</p>

            <p>"This mission represents a fundamental shift in how we approach space exploration," said Mission Director Dr. Amanda Foster. "By demonstrating that private companies can successfully reach Mars, we've opened the door to more frequent, cost-effective missions that could accelerate our understanding of the universe."</p>

            <p>The mission objectives include:
            • Soil and atmospheric analysis for potential life indicators
            • High-resolution mapping of previously unexplored regions
            • Testing of new technologies for future human missions
            • Collection of samples for potential future return to Earth</p>

            <p>NASA and international space agencies have praised the mission's success, noting that collaboration between public and private sectors could revolutionize space exploration and make interplanetary travel more accessible than ever before.</p>
            ''',
            'tags': ['technology', 'innovation', 'exclusive', 'investigation'],
            'featured': True,
            'status': 'published'
        },
        {
            'title': 'Educational Reform Initiative Shows Remarkable Results',
            'category': 'breaking-news',
            'excerpt': 'Comprehensive education reform program demonstrates significant improvements in student performance and graduation rates across participating schools.',
            'content': '''
            <p>A comprehensive educational reform initiative implemented across 500 schools nationwide has demonstrated remarkable results, with participating institutions showing significant improvements in student performance, graduation rates, and college readiness scores.</p>

            <p>The reform program, which focuses on personalized learning approaches, technology integration, and enhanced teacher training, has exceeded all projected outcomes. Students in participating schools have shown a 30% improvement in standardized test scores and a 25% increase in graduation rates.</p>

            <p>Education Secretary Dr. Michael Rodriguez announced the results during a press conference, stating: "These results prove that with the right resources, innovative approaches, and dedicated educators, we can transform the educational experience for all students, regardless of their background or circumstances."</p>

            <p>Key components of the successful program include:
            • Adaptive learning technologies tailored to individual student needs
            • Comprehensive teacher professional development programs
            • Enhanced mental health and wellness support systems
            • Increased parent and community engagement initiatives</p>

            <p>The success has prompted discussions about expanding the program nationally, with federal education officials working to secure funding for implementation in an additional 2,000 schools over the next three years.</p>
            ''',
            'tags': ['breaking', 'trending', 'analysis', 'update'],
            'featured': False,
            'status': 'published'
        }
    ]

    # Create articles with different publish dates
    for i, article_data in enumerate(articles_data):
        # Calculate publish date (spread articles over the last 30 days)
        days_ago = i * 3 + 1  # Space articles 3 days apart
        publish_date = timezone.now() - timedelta(days=days_ago)
        
        # Get category
        category = next(cat for cat in created_categories if cat.slug == article_data['category'])
        
        # Get random author
        author = created_users[i % len(created_users)]
        
        # Create article
        article, created = Article.objects.get_or_create(
            slug=slugify(article_data['title']),
            defaults={
                'title': article_data['title'],
                'author': author,
                'category': category,
                'excerpt': article_data['excerpt'],
                'content': article_data['content'],
                'status': article_data['status'],
                'featured': article_data['featured'],
                'publish_date': publish_date,
                'view_count': (i + 1) * 50  # Simulate view counts
            }
        )
        
        if created:
            # Add tags to the article
            for tag_name in article_data['tags']:
                try:
                    tag = next(tag for tag in created_tags if tag.slug == slugify(tag_name))
                    article.tags.add(tag)
                except StopIteration:
                    pass  # Tag doesn't exist, skip
            
            print(f"✅ Created article: {article.title}")
        else:
            print(f"✅ Using existing article: {article.title}")

    print("\n🎉 Dummy data creation completed successfully!")
    print(f"📊 Created {Category.objects.count()} categories")
    print(f"🏷️ Created {Tag.objects.count()} tags")
    print(f"📰 Created {Article.objects.count()} articles")
    print(f"👥 Total users: {User.objects.count()}")

if __name__ == '__main__':
    print("🚀 Starting dummy data creation for News app...")
    create_dummy_data()
