from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta
from News.models import Category, Tag, Article import Category, Tag, Article

class Command(BaseCommand):
    help = 'Create sample news articles with categories and tags'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Creating sample news data...'))

        # Create or get admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@newsandmedia.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Created admin user'))
        else:
            self.stdout.write(self.style.SUCCESS(f'✅ Using existing admin user'))

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
                self.stdout.write(self.style.SUCCESS(f'✅ Created user: {user.get_full_name()}'))

        # Create categories
        categories_data = [
            {'name': 'Breaking News', 'slug': 'breaking-news', 'description': 'Latest breaking news and urgent updates'},
            {'name': 'Technology', 'slug': 'technology', 'description': 'Tech innovations and digital trends'},
            {'name': 'Politics', 'slug': 'politics', 'description': 'Political news and government updates'},
            {'name': 'Entertainment', 'slug': 'entertainment', 'description': 'Celebrity news and entertainment industry'},
            {'name': 'Health', 'slug': 'health', 'description': 'Health news and medical breakthroughs'},
            {'name': 'Business', 'slug': 'business', 'description': 'Business news and market updates'}
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
                self.stdout.write(self.style.SUCCESS(f'✅ Created category: {category.name}'))

        # Create tags
        tags_data = ['trending', 'urgent', 'exclusive', 'breaking', 'analysis', 'technology', 'politics', 'health']
        created_tags = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(
                slug=slugify(tag_name),
                defaults={'name': tag_name}
            )
            created_tags.append(tag)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Created tag: {tag.name}'))

        # Sample articles data
        articles_data = [
            {
                'title': 'Revolutionary AI Technology Transforms Healthcare Industry',
                'category_slug': 'technology',
                'excerpt': 'A groundbreaking AI system is revolutionizing patient care and diagnosis accuracy across major hospitals worldwide.',
                'content': '''<p>The healthcare industry is experiencing a seismic shift with the introduction of advanced artificial intelligence systems that are transforming patient care and medical diagnostics. This revolutionary technology has been implemented in over 200 hospitals worldwide, showing remarkable improvements in diagnostic accuracy and treatment outcomes.</p>

<p>The AI system, developed by leading technology companies in collaboration with medical professionals, utilizes machine learning algorithms to analyze patient data, medical images, and laboratory results with unprecedented precision. Early trials have shown a 35% improvement in diagnostic accuracy compared to traditional methods.</p>

<p><strong>Key Benefits:</strong></p>
<ul>
<li>35% improvement in diagnostic accuracy</li>
<li>25% reduction in unnecessary procedures</li>
<li>40% decrease in diagnostic wait times</li>
<li>Improved patient outcomes across all departments</li>
</ul>

<p>"This technology represents a paradigm shift in how we approach healthcare," said Dr. Emily Rodriguez, Chief Medical Officer at Metropolitan General Hospital. "The AI's ability to process vast amounts of medical data and identify patterns that might be missed by human analysis is truly remarkable."</p>''',
                'tags': ['technology', 'trending', 'exclusive'],
                'featured': True,
                'status': 'published'
            },
            {
                'title': 'Global Climate Summit Reaches Historic Agreement',
                'category_slug': 'breaking-news',
                'excerpt': 'World leaders unite in unprecedented commitment to achieve net-zero emissions by 2040, setting new global environmental standards.',
                'content': '''<p>In a historic moment for environmental action, world leaders at the Global Climate Summit have reached an unprecedented agreement to achieve net-zero carbon emissions by 2040, moving the deadline forward by a full decade from previous commitments.</p>

<p>The agreement, signed by representatives from 195 countries, includes binding commitments to renewable energy investments, carbon capture technologies, and sustainable development practices.</p>

<p><strong>Key Provisions:</strong></p>
<ul>
<li>$2 trillion in renewable energy investments</li>
<li>Mandatory carbon capture for major industries</li>
<li>Support funds for developing nations</li>
<li>Strict penalties for emission target failures</li>
</ul>

<p>"Today, we've chosen the future of our planet over short-term economic interests," declared UN Climate Chief Maria Santos during the closing ceremony.</p>''',
                'tags': ['breaking', 'urgent', 'politics'],
                'featured': True,
                'status': 'published'
            },
            {
                'title': 'Major Election Updates: Record Voter Turnout Expected',
                'category_slug': 'politics',
                'excerpt': 'Political analysts predict highest voter participation in decades as citizens gear up for crucial elections nationwide.',
                'content': '''<p>Political analysts across the country are predicting record-breaking voter turnout for the upcoming elections, with early voting numbers already surpassing previous records by 40%. This surge in civic engagement reflects the high stakes and intense public interest in this election cycle.</p>

<p>Early voting centers report long lines and enthusiastic participation from voters of all demographics. "We've never seen anything like this," said Election Commissioner Janet Williams.</p>

<p><strong>Driving Factors:</strong></p>
<ul>
<li>Expanded mail-in voting options</li>
<li>Extended early voting periods</li>
<li>Increased voter education campaigns</li>
<li>Heightened public awareness of key issues</li>
</ul>''',
                'tags': ['politics', 'trending'],
                'featured': False,
                'status': 'published'
            },
            {
                'title': 'Entertainment Industry Embraces Virtual Reality',
                'category_slug': 'entertainment',
                'excerpt': 'Major studios announce groundbreaking VR projects that promise to revolutionize audience experiences.',
                'content': '''<p>The entertainment industry is on the brink of a revolutionary transformation as major studios announce ambitious virtual reality projects that will fundamentally change how audiences experience movies, concerts, and live performances.</p>

<p>Leading studios have invested over $500 million in VR technology development, creating immersive experiences that allow viewers to step inside their favorite films and interact with characters in unprecedented ways.</p>

<p>"We're not just watching entertainment anymore; we're living it," explained VR Director Lisa Chen.</p>''',
                'tags': ['technology', 'entertainment'],
                'featured': False,
                'status': 'published'
            },
            {
                'title': 'Medical Breakthrough Offers Hope for Rare Diseases',
                'category_slug': 'health',
                'excerpt': 'Scientists develop innovative gene therapy treatments showing remarkable success rates in treating incurable conditions.',
                'content': '''<p>Medical researchers have achieved a significant breakthrough in gene therapy, developing treatments that show remarkable success rates in addressing rare diseases that were previously considered incurable.</p>

<p>The innovative therapy technique, known as CRISPR-Enhanced Gene Correction (CEGC), has shown success rates exceeding 85% in early clinical trials involving patients with rare genetic disorders.</p>

<p>"What we're seeing is not just treatment, but actual correction of genetic abnormalities at the cellular level," said Dr. Robert Kim, lead researcher.</p>''',
                'tags': ['health', 'exclusive', 'breaking'],
                'featured': False,
                'status': 'published'
            },
            {
                'title': 'Stock Markets Reach All-Time Highs',
                'category_slug': 'business',
                'excerpt': 'Major indices surge to record levels as investor confidence grows following positive economic indicators.',
                'content': '''<p>Global stock markets have reached unprecedented heights this week, with major indices setting new all-time records amid growing investor confidence and positive economic indicators.</p>

<p>The technology sector led the rally, with major tech companies reporting quarterly earnings that exceeded analyst expectations by an average of 25%.</p>

<p><strong>Market Highlights:</strong></p>
<ul>
<li>S&P 500 up 3.2% for the week</li>
<li>Technology sector leading with 5.1% gains</li>
<li>Record trading volumes</li>
<li>International markets following suit</li>
</ul>''',
                'tags': ['business', 'analysis'],
                'featured': False,
                'status': 'published'
            }
        ]

        # Create articles
        for i, article_data in enumerate(articles_data):
            # Get category
            category = Category.objects.get(slug=article_data['category_slug'])
            
            # Get random author
            author = created_users[i % len(created_users)]
            
            # Calculate publish date (spread articles over last 10 days)
            publish_date = timezone.now() - timedelta(days=i + 1)
            
            # Calculate reading time (assume 200 words per minute)
            word_count = len(article_data['content'].split())
            reading_time = max(1, word_count // 200)  # At least 1 minute
            
            # Check if article already exists
            article_slug = slugify(article_data['title'])
            if Article.objects.filter(slug=article_slug).exists():
                article = Article.objects.get(slug=article_slug)
                self.stdout.write(self.style.WARNING(f'⚠️ Article already exists: {article.title}'))
                continue
                
            # Use raw SQL to insert with all required fields since the database has extra fields
            from django.db import connection
            cursor = connection.cursor()
            
            try:
                cursor.execute("""
                    INSERT INTO News_article (
                        title, slug, featured_image, thumbnail, excerpt, content, 
                        featured, reading_time, likes_count, share_count, status, 
                        publish_date, created_at, updated_at, is_featured, views_count, 
                        author_id, category_id, created, view_count, updated
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [
                    article_data['title'],
                    article_slug,
                    '',  # featured_image
                    '',  # thumbnail
                    article_data['excerpt'],
                    article_data['content'],
                    article_data['featured'],
                    reading_time,
                    (i + 1) * 25,  # likes_count
                    (i + 1) * 12,  # share_count
                    article_data['status'],
                    publish_date,
                    publish_date,  # created_at
                    timezone.now(),  # updated_at
                    article_data['featured'],  # is_featured
                    (i + 1) * 87,  # views_count
                    author.id,
                    category.id,
                    publish_date,  # created
                    (i + 1) * 87,  # view_count
                    timezone.now()  # updated
                ])
                
                # Get the created article
                article = Article.objects.get(slug=article_slug)
                created = True
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Error creating article: {e}'))
                continue
            
            if created:
                # Add tags to the article
                for tag_name in article_data['tags']:
                    try:
                        tag = Tag.objects.get(slug=slugify(tag_name))
                        article.tags.add(tag)
                    except Tag.DoesNotExist:
                        pass
                
                self.stdout.write(self.style.SUCCESS(f'✅ Created article: {article.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ Article already exists: {article.title}'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Sample news data creation completed!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total categories: {Category.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'🏷️ Total tags: {Tag.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'📰 Total articles: {Article.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'👥 Total users: {User.objects.count()}'))
