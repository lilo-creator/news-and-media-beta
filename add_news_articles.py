#!/usr/bin/env python
"""
Add news content for Breaking News, Politics, Technology, and Entertainment categories
"""
import os
import django
import sys
from datetime import timedelta
from django.utils import timezone
from django.utils.text import slugify

# Setup Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beta.settings')
django.setup()

from News.models import Article, Category, Tag
from django.contrib.auth.models import User

def create_news():
    # Get or create author
    author, created = User.objects.get_or_create(
        username='editor',
        defaults={
            'email': 'editor@news.com',
            'first_name': 'News',
            'last_name': 'Editor',
            'is_staff': True
        }
    )
    if created:
        author.set_password('editor123')
        author.save()
    
    # Create categories
    categories_data = [
        ('Breaking News', 'breaking-news', 'Latest breaking news and urgent updates'),
        ('Politics', 'politics', 'Political news and government updates'),
        ('Technology', 'technology', 'Tech news, gadgets, and innovations'),
        ('Entertainment', 'entertainment', 'Movies, music, celebrities, and pop culture')
    ]
    
    categories = {}
    for name, slug, desc in categories_data:
        cat, created = Category.objects.get_or_create(
            slug=slug,
            defaults={'name': name, 'description': desc}
        )
        categories[slug] = cat
        print(f"Category: {cat.name}")
    
    # Create articles with images
    articles = [
        {
            'title': 'BREAKING: Major Trade Agreement Signed Between Global Powers',
            'category': 'breaking-news',
            'excerpt': 'Historic trade deal promises to reshape international commerce and boost global economy.',
            'content': '''In a landmark ceremony today, representatives from the world's largest economies signed a comprehensive trade agreement that economists predict will boost global GDP by 3.5% over the next five years.

The agreement includes:
• Reduced tariffs on over 5,000 product categories
• Streamlined customs procedures
• Enhanced digital trade provisions
• Environmental protection standards
• Labor rights protections

"This agreement represents a new era of international cooperation," said lead negotiator Sarah Chen. "We've created a framework that benefits workers, businesses, and consumers worldwide."

The deal comes after 18 months of intensive negotiations and covers trade worth over $15 trillion annually. Implementation begins January 1st, with full benefits expected by 2027.

Key provisions include immediate tariff reductions on technology products, gradual elimination of agricultural barriers, and new rules for digital services that reflect the modern economy.

Opposition leaders have raised concerns about potential job displacement in certain sectors, though supporters argue the overall economic benefits will create more opportunities than are lost.''',
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Emergency Response Teams Deploy as Severe Weather Hits Region',
            'category': 'breaking-news', 
            'excerpt': 'Multiple states declare emergency as unprecedented storm system brings flooding and power outages.',
            'content': '''Emergency management agencies across three states have activated disaster response protocols as a massive storm system brings dangerous conditions including flash flooding, damaging winds, and widespread power outages.

Current situation:
• 200,000+ homes without power
• Flash flood warnings in 15 counties  
• Wind gusts up to 80 mph recorded
• 12 emergency shelters opened
• Major highways closed due to flooding

Governor Martinez declared a state of emergency, enabling rapid deployment of National Guard units to assist with evacuations and emergency response.

"Public safety is our top priority," said Emergency Management Director Robert Kim. "We urge residents to stay indoors and avoid all non-essential travel until conditions improve."

The storm is expected to weaken over the next 24 hours, but flooding concerns will persist through the weekend as rivers crest above flood stage.

Utility companies have deployed additional crews from neighboring states to restore power, with full restoration expected by Tuesday.''',
            'status': 'published',
            'featured': False
        },
        {
            'title': 'Congressional Committee Approves Infrastructure Modernization Bill',
            'category': 'politics',
            'excerpt': 'Bipartisan legislation advances with $800 billion investment in roads, bridges, and broadband.',
            'content': '''The House Infrastructure Committee voted 28-14 today to advance comprehensive infrastructure legislation that would authorize $800 billion in federal spending over the next decade.

The bill includes:
• $350 billion for highway and bridge repairs
• $200 billion for broadband expansion
• $150 billion for clean energy infrastructure  
• $100 billion for public transportation

Committee Chair Representative Johnson emphasized the bipartisan nature of the effort: "This bill addresses critical needs that affect every American community, from rural broadband access to urban transit systems."

The legislation now moves to the full House for consideration next week, where it's expected to pass with strong bipartisan support.

Key provisions include Buy American requirements for infrastructure projects, prevailing wage standards for construction workers, and environmental review streamlining to accelerate project timelines.

The Congressional Budget Office estimates the bill would create 2.3 million jobs over five years while generating long-term economic benefits through improved transportation efficiency and expanded digital connectivity.

Opposition has focused primarily on funding mechanisms and the federal government's role in traditionally state-managed infrastructure projects.''',
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Presidential Approval Rating Climbs Following Economic Gains',
            'category': 'politics',
            'excerpt': 'New polling shows 58% approval as unemployment drops and GDP growth exceeds expectations.',
            'content': '''A new national poll shows President Anderson's approval rating has climbed to 58%, the highest level in 14 months, as voters respond positively to strong economic indicators and legislative achievements.

The survey of 1,200 registered voters shows significant improvement across key issues:
• Overall job approval: 58% (up from 51%)
• Economic handling: 62% approval
• Foreign policy: 54% approval  
• Healthcare: 56% approval

The rating surge coincides with positive economic news including unemployment falling to 3.7%, GDP growth of 4.1% last quarter, and consumer confidence reaching a three-year high.

Political analyst Dr. Maria Rodriguez noted: "These numbers reflect growing confidence in the administration's policy agenda. The infrastructure bill and economic recovery are clearly resonating with voters."

The poll also shows strong regional variations, with approval highest in suburban areas (61%) and more moderate in rural regions (52%). Urban voters showed 65% approval.

Key demographic shifts include improved standing among independent voters (55% approval) and college-educated women (67% approval), both crucial swing groups for upcoming elections.

"While these are encouraging numbers, we remain focused on delivering results for American families," said White House Press Secretary Thompson during today's briefing.''',
            'status': 'published',
            'featured': False
        },
        {
            'title': 'Revolutionary AI Chip Achieves Quantum-Level Performance Breakthrough',
            'category': 'technology',
            'excerpt': 'Tech giant unveils processor that delivers 50x speed improvement for artificial intelligence tasks.',
            'content': '''Silicon Valley innovator QuantumTech announced today a revolutionary AI processor chip that delivers unprecedented performance gains, achieving computation speeds previously thought impossible with current technology.

The new "NeuralMax" chip specifications:
• 50x faster AI model training
• 70% reduction in power consumption
• Support for models with 10 trillion parameters
• Real-time processing of complex neural networks
• Built-in quantum error correction

CEO Dr. Lisa Park demonstrated the chip's capabilities during a live presentation, showing AI models that typically require hours of training completing in just minutes.

"This isn't just an incremental improvement," Park explained. "We've fundamentally reimagined how silicon can process artificial intelligence workloads."

The breakthrough utilizes a hybrid architecture combining traditional processors with quantum-inspired computing elements, enabling parallel processing at unprecedented scales.

Early partners report remarkable results:
• Autonomous vehicle companies achieving real-time decision making
• Medical researchers accelerating drug discovery by 10x
• Language models providing human-like responses instantly
• Financial firms running complex risk analysis in seconds

The chip will be available to enterprise customers starting Q2 2025, with consumer applications expected by late 2025. Industry analysts predict this could accelerate AI adoption across industries and make advanced AI accessible to smaller companies.

Stock markets responded enthusiastically, with QuantumTech shares rising 23% in after-hours trading.''',
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Major Social Platform Launches Advanced Privacy Protection Features',
            'category': 'technology',
            'excerpt': 'New encryption and data control tools give users unprecedented control over personal information.',
            'content': '''Social media giant ConnectWorld today announced a comprehensive suite of privacy protection features that give users unprecedented control over their personal data and communications.

New features include:
• End-to-end encryption for all messages and posts
• Granular data sharing controls
• AI-powered privacy assistant
• One-click data export and deletion
• Anonymous browsing modes

"Privacy is not a luxury—it's a fundamental right," said Chief Privacy Officer Amanda Chen during the feature announcement. "These tools put users in complete control of their digital footprint."

The rollout addresses growing concerns about data privacy and follows increased regulatory scrutiny of social media platforms' data practices.

Key capabilities:
- Users can now encrypt individual posts or entire profiles
- New permission system requires explicit consent for data sharing
- AI assistant automatically detects and warns about privacy risks
- Enhanced settings allow custom privacy rules for different content types

The platform has also committed to annual third-party privacy audits and published detailed data usage reports showing exactly how user information is processed and shared.

Privacy advocates have praised the moves while noting that effective implementation will be crucial for user adoption.

The new features begin rolling out next week to premium subscribers, with full availability for all users by year-end. The company estimates 90% of users will activate at least some privacy features within the first month.''',
            'status': 'published',
            'featured': False
        },
        {
            'title': 'Blockbuster Fantasy Epic Dominates Global Box Office Rankings',
            'category': 'entertainment',
            'excerpt': 'Dragons of Eternity breaks multiple opening weekend records with $485 million worldwide.',
            'content': '''The highly anticipated fantasy epic "Dragons of Eternity" shattered multiple box office records this weekend, earning an unprecedented $485 million globally in its opening four days.

Box office breakdown:
• Domestic (US/Canada): $198 million
• International markets: $287 million
• IMAX/Premium formats: $89 million (18% of total)
• Thursday preview screenings: $45 million

The film surpassed the previous opening record held by "Galactic Warriors: Final Battle" ($412 million) and represents the biggest fantasy film debut in cinema history.

Director Michael Torres expressed amazement at the global response: "We knew we had something special, but this reception has exceeded our wildest dreams. Audiences worldwide are connecting with these characters and this world."

Critical and audience reception:
- 94% Fresh on Rotten Tomatoes (critics)
- 96% Audience Score
- A+ CinemaScore from opening audiences
- 9.2/10 average rating on movie databases

The film features groundbreaking visual effects with over 3,200 VFX shots created by teams in seven countries. The production employed cutting-edge motion capture technology to bring the dragon characters to life with unprecedented realism.

Star Emma Wilson, who plays the dragon rider protagonist, commented: "This story celebrates the power of courage and friendship. Knowing that families around the world are experiencing this adventure together is incredibly meaningful."

International highlights:
- China: $52 million (biggest fantasy opening ever)
- UK: $31 million  
- Germany: $24 million
- Japan: $28 million
- Australia: $19 million

Industry analysts project the film could reach $1.5 billion globally, potentially making it one of the highest-grossing films of all time.''',
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Grammy-Winning Artist Announces Surprise Album and World Tour',
            'category': 'entertainment',
            'excerpt': 'Platinum recording star drops new album at midnight, reveals 60-city global tour dates.',
            'content': '''Multi-Grammy winner Jordan Rivers surprised fans worldwide at midnight with the unexpected release of "Midnight Reflections," a deeply personal album exploring themes of growth, love, and resilience.

The 14-track album features collaborations with several acclaimed artists and showcases Rivers' evolution as both a songwriter and performer since their last release three years ago.

Album highlights:
• Lead single "Phoenix Rising" already trending globally
• Collaborations with three Grammy winners
• Mix of intimate acoustic tracks and powerful anthems  
• Personal lyrics addressing recent life changes
• Production by legendary producer Marcus Gold

"This album represents my most honest work," Rivers shared on social media. "Every song tells part of my story over these past few years."

Accompanying the album announcement, Rivers revealed "The Reflection Tour"—a 60-city world tour spanning 18 months across North America, Europe, Asia, and Australia.

Tour features:
- Innovative 360-degree stage design
- Live orchestra for select songs
- Intimate acoustic segments
- Special guests varying by location
- Portion of proceeds supporting music education

Pre-sale tickets for fan club members begin Thursday, with general sales starting Saturday. VIP packages include meet-and-greet opportunities and exclusive merchandise.

The surprise release strategy paid off immediately, with streaming platforms reporting the album broke several first-day records. Social media buzz generated over 5 million mentions in the first 12 hours.

Music industry executive Sarah Kim noted: "Jordan's ability to connect emotionally with audiences is unparalleled. This album and tour will likely be among the year's biggest cultural events."''',
            'status': 'published',
            'featured': False
        }
    ]
    
    # Create articles
    created = 0
    for data in articles:
        cat_slug = data.pop('category')
        data['category'] = categories[cat_slug]
        data['author'] = author
        data['slug'] = slugify(data['title'])
        data['publish_date'] = timezone.now() - timedelta(days=created)
        
        if not Article.objects.filter(slug=data['slug']).exists():
            Article.objects.create(**data)
            created += 1
            print(f"Created: {data['title']}")
    
    print(f"\nCreated {created} articles")
    print(f"Total articles: {Article.objects.count()}")
    print(f"Categories: {Category.objects.count()}")

if __name__ == '__main__':
    create_news()
