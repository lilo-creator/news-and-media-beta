from django.views.generic import TemplateView

def get_dummy_articles():
    """Return a list of dummy news articles that can be used by both views."""
    return [
        {
            'title': 'New AI Technology Breakthrough Promises Revolutionary Changes',
            'slug': 'new-ai-technology-breakthrough',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1932&auto=format&fit=crop',
            'excerpt': 'Scientists have developed a new AI system that can understand and respond to human emotions with unprecedented accuracy, opening doors to applications in healthcare and education.',
            'featured': True,
            'category': {'name': 'Technology', 'slug': 'technology'},
            'publish_date': '2025-07-25',
            'view_count': 1250,
            'author': {'get_full_name': 'John Smith'}
        },
        {
            'title': 'Global Summit on Climate Change Reaches Landmark Agreement',
            'slug': 'global-climate-summit-agreement',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1610552050890-fe99536c2615?q=80&w=1932&auto=format&fit=crop',
            'excerpt': 'World leaders have agreed on a new set of ambitious targets to reduce carbon emissions by 2035, with major economic powers committing to significant investments in renewable energy.',
            'featured': True,
            'category': {'name': 'Politics', 'slug': 'politics'},
            'publish_date': '2025-07-24',
            'view_count': 982,
            'author': {'get_full_name': 'Maria Johnson'}
        },
        {
            'title': 'Major Medical Breakthrough in Cancer Treatment',
            'slug': 'cancer-treatment-breakthrough',
            'get_featured_image_url': 'https://media.istockphoto.com/id/1477482163/photo/doctor-healthcare-or-finger-on-xray-hologram-in-tuberculosis-virus-cancer-analytics-or-asthma.jpg?s=1024x1024&w=is&k=20&c=m_1i1T9MuGtxw7mzCf9zWxI7q9_6a_51JCBYhlURIhw=',
            'excerpt': 'Researchers announce a promising new therapy that has shown remarkable results in clinical trials, potentially offering hope for patients with previously untreatable forms of cancer.',
            'featured': False,
            'category': {'name': 'Health', 'slug': 'health'},
            'publish_date': '2025-07-23',
            'view_count': 785,
            'author': {'get_full_name': 'Robert Chen'}
        },
        {
            'title': 'Tech Giant Launches Revolutionary New Smartphone',
            'slug': 'tech-giant-new-smartphone',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?q=80&w=1470&auto=format&fit=crop',
            'excerpt': 'The latest flagship device features groundbreaking technology that sets new standards for the industry, including a foldable display and unprecedented battery life.',
            'featured': False,
            'category': {'name': 'Technology', 'slug': 'technology'},
            'publish_date': '2025-07-22',
            'view_count': 1568,
            'author': {'get_full_name': 'Lisa Wong'}
        },
        {
            'title': 'Global Stock Markets Hit All-Time High',
            'slug': 'global-stock-markets-high',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=1470&auto=format&fit=crop',
            'excerpt': 'Major indices around the world are reaching record levels as investor confidence soars, driven by strong corporate earnings and positive economic indicators.',
            'featured': False,
            'category': {'name': 'Business', 'slug': 'business'},
            'publish_date': '2025-07-21',
            'view_count': 964,
            'author': {'get_full_name': 'Alex Martinez'}
        },
        {
            'title': 'Award-Winning Film Director Announces New Project',
            'slug': 'film-director-new-project',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=1459&auto=format&fit=crop',
            'excerpt': 'The acclaimed filmmaker is set to begin production on an eagerly anticipated sci-fi thriller, featuring an ensemble cast of A-list actors and groundbreaking visual effects.',
            'featured': False,
            'category': {'name': 'Entertainment', 'slug': 'entertainment'},
            'publish_date': '2025-07-20',
            'view_count': 845,
            'author': {'get_full_name': 'Emma Davis'}
        },
        {
            'title': 'Renewable Energy Investments Reach Record High',
            'slug': 'renewable-energy-investments',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?q=80&w=1472&auto=format&fit=crop',
            'excerpt': 'Global investments in clean energy technologies have surpassed fossil fuels for the first time, marking a historic shift in the world\'s approach to power generation and climate change.',
            'featured': False,
            'category': {'name': 'Business', 'slug': 'business'},
            'publish_date': '2025-07-19',
            'view_count': 723,
            'author': {'get_full_name': 'Thomas Lee'}
        },
        {
            'title': 'Major Security Vulnerability Discovered in Popular Software',
            'slug': 'security-vulnerability-software',
            'get_featured_image_url': 'https://images.pexels.com/photos/938165/pexels-photo-938165.jpeg',
            'excerpt': 'Cybersecurity experts urge immediate updates as critical flaw affects millions of users worldwide, with potential for data breaches and unauthorized access to sensitive information.',
            'featured': False,
            'category': {'name': 'Technology', 'slug': 'technology'},
            'publish_date': '2025-07-18',
            'view_count': 1125,
            'author': {'get_full_name': 'Sarah Johnson'}
        },
        {
            'title': 'New Health Guidelines Recommend Changes to Daily Diet',
            'slug': 'new-health-diet-guidelines',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=1470&auto=format&fit=crop',
            'excerpt': 'Health authorities release updated nutritional advice focusing on balanced intake and reduced processed foods, emphasizing the importance of plant-based options and mindful eating practices.',
            'featured': False,
            'category': {'name': 'Health', 'slug': 'health'},
            'publish_date': '2025-07-17',
            'view_count': 673,
            'author': {'get_full_name': 'Daniel Williams'}
        },
        {
            'title': 'International Space Mission Successfully Lands on Mars',
            'slug': 'mars-landing-mission',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?q=80&w=1474&auto=format&fit=crop',
            'excerpt': 'The multinational spacecraft has touched down safely on the Martian surface, beginning a new chapter in interplanetary exploration with advanced scientific instruments and sample collection capabilities.',
            'featured': False,
            'category': {'name': 'Science', 'slug': 'science'},
            'publish_date': '2025-07-16',
            'view_count': 2145,
            'author': {'get_full_name': 'Priya Sharma'}
        },
        {
            'title': 'Breakthrough in Quantum Computing Achieves New Milestone',
            'slug': 'quantum-computing-milestone',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=1470&auto=format&fit=crop',
            'excerpt': 'Scientists have successfully maintained quantum coherence for a record duration, bringing practical quantum computing applications significantly closer to reality and challenging existing encryption methods.',
            'featured': False,
            'category': {'name': 'Technology', 'slug': 'technology'},
            'publish_date': '2025-07-15',
            'view_count': 1836,
            'author': {'get_full_name': 'Michael Chen'}
        },
        {
            'title': 'Historic Peace Agreement Signed in Middle East',
            'slug': 'middle-east-peace-agreement',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?q=80&w=1435&auto=format&fit=crop',
            'excerpt': 'After decades of conflict, regional powers have reached a comprehensive peace accord that addresses territorial disputes, security concerns, and economic cooperation frameworks.',
            'featured': True,
            'category': {'name': 'Politics', 'slug': 'politics'},
            'publish_date': '2025-07-14',
            'view_count': 3245,
            'author': {'get_full_name': 'Omar Hassan'}
        }
    ]

class NewsListView(TemplateView):
    template_name = 'News/news_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = get_dummy_articles()
        context['categories'] = [
            {'name': 'Technology', 'slug': 'technology'},
            {'name': 'Politics', 'slug': 'politics'},
            {'name': 'Health', 'slug': 'health'},
            {'name': 'Business', 'slug': 'business'},
            {'name': 'Entertainment', 'slug': 'entertainment'},
            {'name': 'Science', 'slug': 'science'},
            {'name': 'Sports', 'slug': 'sports'},
            {'name': 'Education', 'slug': 'education'}
        ]
        
        # Only apply filtering if this is a direct request (not when called from DetailView)
        # and no_filtering is not set
        if hasattr(self, 'request') and not kwargs.get('no_filtering', False):
            # Filter articles by category if category parameter is provided in the URL
            category_slug = self.request.GET.get('category')
            if category_slug:
                context['articles'] = [article for article in context['articles'] 
                                      if article['category']['slug'] == category_slug]
                                      
            # Handle search functionality
            search_query = self.request.GET.get('search')
            if search_query:
                search_query = search_query.lower()
                context['articles'] = [article for article in context['articles'] 
                                      if search_query in article['title'].lower() or 
                                         search_query in article['excerpt'].lower()]
        
        return context

class NewsDetailView(TemplateView):
    template_name = 'News/news_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        
        # Get all articles from the shared function
        articles = get_dummy_articles()
        
        # Find the article with the matching slug
        article = next((a for a in articles if a['slug'] == slug), None)
        
        if not article:
            # If no matching article found, use the first article as a default
            article = articles[0]
            
        # Add detailed content to the article
        article_content = self.get_article_content(slug)
        article['content'] = article_content
        
        # Add tags to the article
        article['tags'] = {
            'all': self.get_article_tags(slug)
        }
        
        # Add comments to the article
        article['comments'] = {
            'all': self.get_article_comments(slug)
        }
        
        # Get related articles (3 articles excluding the current one)
        related_articles = [a for a in articles if a['slug'] != slug][:3]
        
        context['article'] = article
        context['related_articles'] = related_articles
        return context
        
    def get_article_content(self, slug):
        """Get detailed content for a specific article."""
        content_mapping = {
            'new-ai-technology-breakthrough': """
                <p class="lead">In a groundbreaking development that promises to revolutionize how machines interact with humans, researchers at the Advanced Neural Systems Institute have unveiled a new AI system capable of understanding and responding to human emotions with unprecedented accuracy.</p>
                
                <p>The system, named EmotionAI, utilizes a complex neural network architecture that processes multiple sensory inputs simultaneously—including facial expressions, voice tonality, and physiological signals—to identify emotional states with over 95% accuracy, a significant improvement over previous systems that typically achieved 75-80% accuracy.</p>
                
                <h3>Technological Breakthrough</h3>
                
                <p>"What makes EmotionAI truly revolutionary is its ability to learn and adapt to individual emotional patterns over time," explains Dr. Eleanor Chen, lead researcher on the project. "The system doesn't just recognize emotions based on universal markers; it develops a personalized emotional profile for each user, allowing for increasingly nuanced understanding."</p>
                
                <p>The technology incorporates several innovative components:</p>
                
                <ul>
                    <li>Multi-modal sensory integration algorithms that combine visual, auditory, and biometric data</li>
                    <li>A reinforcement learning framework that continuously improves accuracy through interaction</li>
                    <li>Ethical safeguards designed to protect user privacy and prevent manipulation</li>
                    <li>Cultural context adaptation to account for differences in emotional expression across societies</li>
                </ul>
                
                <blockquote class="blockquote">
                    <p>This represents a significant advancement in human-computer interaction that will have far-reaching implications for healthcare, education, and interpersonal communication technologies.</p>
                    <footer class="blockquote-footer">Dr. Marcus Williams, Director of the Institute for Cognitive Computing</footer>
                </blockquote>
                
                <h3>Practical Applications</h3>
                
                <p>The development team envisions numerous applications for EmotionAI, particularly in healthcare and education. In therapeutic settings, the technology could help monitor patients' emotional responses during treatment, providing valuable insights for mental health professionals. In educational environments, it could adapt teaching methods based on students' engagement and frustration levels.</p>
                
                <p>However, the technology also raises important ethical questions about privacy, consent, and the potential for emotional manipulation. The research team has emphasized their commitment to responsible development, including the implementation of strict data protection protocols and transparent AI decision-making processes.</p>
                
                <h3>Future Directions</h3>
                
                <p>The team plans to begin limited real-world testing of EmotionAI in controlled healthcare and educational settings later this year, following approval from ethical review boards. These pilot programs will focus on gathering data about the system's effectiveness and addressing any unforeseen issues before wider deployment is considered.</p>
                
                <p>Industry analysts predict that emotion-aware AI systems could become a $25 billion market by 2030, with applications extending into customer service, entertainment, automotive safety, and personal devices. As the technology matures, it could fundamentally change how we interact with machines and, potentially, with each other.</p>
            """,
            'global-climate-summit-agreement': """
                <p class="lead">In what many are calling a historic breakthrough, world leaders attending the Global Climate Summit in Geneva have reached a landmark agreement on aggressive new targets to combat climate change, with major economic powers committing to significant reductions in carbon emissions by 2035.</p>
                
                <p>The agreement, finalized after two weeks of intense negotiations, establishes a binding framework for nations to reduce global carbon emissions by 60% from 2020 levels within the next decade. This represents a substantial increase from the previous international target of 40% reductions by 2040.</p>
                
                <h3>Key Provisions</h3>
                
                <p>The new climate accord includes several groundbreaking provisions:</p>
                
                <ul>
                    <li>A commitment from all G20 nations to achieve carbon neutrality in their energy sectors by 2035</li>
                    <li>The establishment of a $500 billion "Green Transition Fund" to help developing nations build renewable energy infrastructure</li>
                    <li>A global carbon pricing mechanism to be implemented by 2027</li>
                    <li>Mandatory climate risk disclosure requirements for multinational corporations</li>
                    <li>A phase-out of all new fossil fuel exploration by 2030</li>
                </ul>
                
                <p>"This agreement represents the kind of bold, cooperative action the world has been waiting for," said UN Secretary-General Amara Okafor. "For the first time, we have commitments that match the scale of the climate crisis we face."</p>
                
                <blockquote class="blockquote">
                    <p>The science has been clear for decades. What's different today is that the economic and political will has finally aligned with that science. This agreement gives us a fighting chance to prevent the worst impacts of climate change.</p>
                    <footer class="blockquote-footer">Dr. Sophia Mendez, Climate Scientist at the International Climate Research Institute</footer>
                </blockquote>
                
                <h3>Economic Implications</h3>
                
                <p>The agreement has significant economic implications, particularly for the energy and transportation sectors. Many fossil fuel companies saw their stock prices decline following the announcement, while renewable energy stocks surged. Automotive manufacturers with strong electric vehicle programs also saw gains.</p>
                
                <p>Economists project that the agreement will accelerate the already ongoing transition to renewable energy, potentially creating millions of new jobs in solar, wind, and other clean energy sectors. However, communities currently dependent on fossil fuel extraction may face challenging economic adjustments.</p>
                
                <h3>Implementation Challenges</h3>
                
                <p>Despite the enthusiasm surrounding the agreement, significant challenges remain for its implementation. Some nations with large fossil fuel reserves have expressed concerns about the pace of transition, and questions remain about monitoring and enforcement mechanisms.</p>
                
                <p>"The real test will be translating these commitments into concrete policy changes at the national level," noted climate policy expert Dr. James Chen. "We've seen ambitious international agreements before that failed to deliver the promised results."</p>
                
                <p>The agreement establishes a robust monitoring and verification system, including regular progress reviews beginning in 2027. Nations that fail to meet their commitments may face trade measures under the agreement's enforcement provisions.</p>
            """,
            'cancer-treatment-breakthrough': """
                <p class="lead">Medical researchers at the Global Oncology Institute have announced a potentially game-changing breakthrough in cancer treatment, publishing results from a Phase II clinical trial of a novel therapy that shows remarkable effectiveness against previously untreatable forms of aggressive cancer.</p>
                
                <p>The treatment, called Immuno-Target Therapy (ITT), combines precision genetic targeting with enhanced immunotherapy to identify and destroy cancer cells with unprecedented specificity, while leaving healthy tissue largely unaffected. In the clinical trial, 78% of patients with advanced, treatment-resistant tumors showed significant improvement, with 45% experiencing complete remission.</p>
                
                <h3>Revolutionary Approach</h3>
                
                <p>"What makes ITT fundamentally different from existing treatments is its two-pronged approach," explains Dr. Leila Patel, lead researcher on the study. "First, we use advanced genetic sequencing to identify unique markers on a patient's specific cancer cells. Then, we engineer the patient's own immune cells to recognize these markers with extreme precision, essentially creating a customized cancer-fighting force for each individual."</p>
                
                <p>The therapy builds on recent advances in both gene editing and immunotherapy, but combines them in a novel way that appears to overcome many limitations of current treatments:</p>
                
                <ul>
                    <li>Higher precision targeting that minimizes damage to healthy cells</li>
                    <li>Effectiveness against solid tumors, which have been resistant to many immunotherapies</li>
                    <li>Significantly reduced side effects compared to traditional chemotherapy</li>
                    <li>Potential long-term protection against cancer recurrence</li>
                </ul>
                
                <blockquote class="blockquote">
                    <p>In my forty years of oncology research, I've never seen results this promising for patients who had exhausted all other options. This could represent a paradigm shift in how we approach cancer treatment.</p>
                    <footer class="blockquote-footer">Dr. Martin Rodriguez, Director of the National Cancer Research Center</footer>
                </blockquote>
                
                <h3>Patient Experiences</h3>
                
                <p>Among the trial participants was Elaine Summers, 56, who had been battling an aggressive form of pancreatic cancer for three years and had exhausted all standard treatment options. "After two months on the ITT protocol, my scans showed a 90% reduction in tumor size," Summers reported. "I've gone from planning my funeral to planning my future."</p>
                
                <p>While not all patients responded as dramatically, the overall results far exceeded expectations for a Phase II trial involving patients with such advanced disease. Importantly, the side effects were generally mild to moderate, primarily consisting of temporary flu-like symptoms as the immune system activated.</p>
                
                <h3>Next Steps</h3>
                
                <p>The research team has already received expedited approval to begin a larger Phase III clinical trial, which will involve over 2,000 patients across 15 countries. This expanded study will help determine whether the treatment is equally effective across different cancer types and genetic profiles.</p>
                
                <p>"While we\'re extremely encouraged by these results, we need to be cautious about declaring victory too soon," Dr. Patel emphasized. "The Phase III trial will give us much more comprehensive data on effectiveness, optimal protocols, and long-term outcomes."</p>
                
                <p>If the Phase III results confirm the current findings, ITT could receive regulatory approval and become widely available within three years. The research team is already working with healthcare systems to develop the infrastructure needed to deliver this personalized treatment approach to patients worldwide.</p>
            """,
            # Default content for other articles
            'default': """
                <p class="lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                
                <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                
                <h3>Key Developments</h3>
                
                <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
                
                <ul>
                    <li>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit</li>
                    <li>Sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt</li>
                    <li>Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur</li>
                </ul>
                
                <blockquote class="blockquote">
                    <p>This represents a significant advancement in our field and will have far-reaching implications for years to come.</p>
                    <footer class="blockquote-footer">Industry Expert</footer>
                </blockquote>
                
                <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.</p>
                
                <h3>Future Implications</h3>
                
                <p>Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.</p>
                
                <p>Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.</p>
            """
        }
        
        return content_mapping.get(slug, content_mapping['default'])
        
    def get_article_tags(self, slug):
        """Get tags for a specific article."""
        tags_mapping = {
            'new-ai-technology-breakthrough': [
                {'name': 'Artificial Intelligence', 'slug': 'artificial-intelligence'},
                {'name': 'Technology', 'slug': 'technology'},
                {'name': 'Innovation', 'slug': 'innovation'},
                {'name': 'Machine Learning', 'slug': 'machine-learning'},
                {'name': '2025', 'slug': '2025'}
            ],
            'global-climate-summit-agreement': [
                {'name': 'Climate Change', 'slug': 'climate-change'},
                {'name': 'Politics', 'slug': 'politics'},
                {'name': 'Environment', 'slug': 'environment'},
                {'name': 'International', 'slug': 'international'},
                {'name': 'Policy', 'slug': 'policy'}
            ],
            'cancer-treatment-breakthrough': [
                {'name': 'Healthcare', 'slug': 'healthcare'},
                {'name': 'Medical Research', 'slug': 'medical-research'},
                {'name': 'Cancer', 'slug': 'cancer'},
                {'name': 'Innovation', 'slug': 'innovation'},
                {'name': 'Science', 'slug': 'science'}
            ]
        }
        
        default_tags = [
            {'name': 'News', 'slug': 'news'},
            {'name': 'Trending', 'slug': 'trending'},
            {'name': '2025', 'slug': '2025'}
        ]
        
        return tags_mapping.get(slug, default_tags)
        
    def get_article_comments(self, slug):
        """Get comments for a specific article."""
        comments_mapping = {
            'new-ai-technology-breakthrough': [
                {
                    'name': 'Jane Cooper',
                    'created_at': '2025-07-26',
                    'body': 'This technology sounds incredible, but I worry about the privacy implications. How will they ensure our emotional data isn\'t misused?',
                    'is_parent': True
                },
                {
                    'name': 'Robert Johnson',
                    'created_at': '2025-07-26',
                    'body': 'As someone working in the AI field, I can say this is a genuine breakthrough. The multi-modal approach they\'re using is something researchers have been trying to perfect for years.',
                    'is_parent': True
                },
                {
                    'name': 'Emily Chen',
                    'created_at': '2025-07-27',
                    'body': 'I can see huge applications for this in education. Imagine learning programs that can tell when students are confused or frustrated and adjust accordingly.',
                    'is_parent': True
                }
            ],
            'global-climate-summit-agreement': [
                {
                    'name': 'Thomas Lee',
                    'created_at': '2025-07-25',
                    'body': 'Finally some real action! But I\'m skeptical about enforcement. What happens if countries don\'t meet their targets?',
                    'is_parent': True
                },
                {
                    'name': 'Maria Rodriguez',
                    'created_at': '2025-07-25',
                    'body': 'This is a crucial step forward, but we need to ensure the transition is just and equitable for communities that currently depend on fossil fuel industries.',
                    'is_parent': True
                }
            ],
            'cancer-treatment-breakthrough': [
                {
                    'name': 'David Wilson',
                    'created_at': '2025-07-24',
                    'body': 'My mother is battling stage 4 cancer. How can patients get involved in the Phase III trials? This gives us so much hope.',
                    'is_parent': True
                },
                {
                    'name': 'Sarah Johnson',
                    'created_at': '2025-07-24',
                    'body': 'As an oncology nurse, I\'m cautiously optimistic. We\'ve seen promising treatments before that didn\'t pan out in larger trials, but this approach makes a lot of sense theoretically.',
                    'is_parent': True
                },
                {
                    'name': 'Michael Brown',
                    'created_at': '2025-07-25',
                    'body': 'The reduced side effects alone would be revolutionary. Current treatments are so brutal on patients.',
                    'is_parent': True
                }
            ]
        }
        
        default_comments = [
            {
                'name': 'User123',
                'created_at': '2025-07-26',
                'body': 'Interesting article! Thanks for sharing this information.',
                'is_parent': True
            },
            {
                'name': 'NewsReader',
                'created_at': '2025-07-26',
                'body': 'I appreciate the detailed reporting on this topic.',
                'is_parent': True
            }
        ]
        
        return comments_mapping.get(slug, default_comments)
