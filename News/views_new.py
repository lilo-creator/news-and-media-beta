from django.views.generic import TemplateView

class NewsListView(TemplateView):
    template_name = 'News/news_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = [
            {
                'title': 'New AI Technology Breakthrough',
                'slug': 'new-ai-technology-breakthrough',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1932&auto=format&fit=crop',
                'excerpt': 'Scientists have developed a new AI system that can understand and respond to human emotions.',
                'featured': True,
                'category': {'name': 'Technology', 'slug': 'technology'},
                'publish_date': '2025-07-25',
                'view_count': 1250,
                'author': {'get_full_name': 'John Smith'}
            },
            {
                'title': 'Global Climate Summit Agreement',
                'slug': 'global-climate-summit-agreement',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1610552050890-fe99536c2615?q=80&w=1932&auto=format&fit=crop',
                'excerpt': 'World leaders have agreed on ambitious targets to reduce emissions.',
                'featured': True,
                'category': {'name': 'Politics', 'slug': 'politics'},
                'publish_date': '2025-07-24',
                'view_count': 982,
                'author': {'get_full_name': 'Maria Johnson'}
            }
        ]
        context['categories'] = [
            {'name': 'Technology', 'slug': 'technology'},
            {'name': 'Politics', 'slug': 'politics'},
            {'name': 'Health', 'slug': 'health'}
        ]
        return context

class NewsDetailView(TemplateView):
    template_name = 'News/news_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        
        # Dummy article
        article = {
            'title': 'New AI Technology Breakthrough',
            'slug': 'new-ai-technology-breakthrough',
            'get_featured_image_url': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1932&auto=format&fit=crop',
            'excerpt': 'Scientists have developed a new AI system that can understand and respond to human emotions.',
            'content': '<p>This is a sample article content.</p><p>More content here.</p>',
            'featured': True,
            'category': {'name': 'Technology', 'slug': 'technology'},
            'publish_date': '2025-07-25',
            'view_count': 1250,
            'author': {'get_full_name': 'John Smith'},
            'tags': {'all': [{'name': 'AI', 'slug': 'ai'}, {'name': 'Tech', 'slug': 'tech'}]},
            'comments': {'all': [{'name': 'Jane Cooper', 'created_at': '2025-07-26', 'body': 'Great article!', 'is_parent': True}]}
        }
        
        context['article'] = article
        context['related_articles'] = [
            {
                'title': 'Global Climate Summit Agreement',
                'slug': 'global-climate-summit-agreement',
                'get_featured_image_url': 'https://images.unsplash.com/photo-1610552050890-fe99536c2615?q=80&w=1932&auto=format&fit=crop',
                'excerpt': 'World leaders have agreed on ambitious targets to reduce emissions.',
                'category': {'name': 'Politics', 'slug': 'politics'}
            }
        ]
        return context
