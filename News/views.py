from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.db.models import Q

class NewsListView(ListView):
    model = Article
    template_name = 'News/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 9
    ordering = ['-publish_date']

    def get_queryset(self):
        queryset = super().get_queryset().filter(status='published')
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        
        if category:
            queryset = queryset.filter(category__slug=category)
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(excerpt__icontains=search)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category')
        context['current_search'] = self.request.GET.get('search')
        return context

class NewsDetailView(DetailView):
    model = Article
    template_name = 'News/news_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        
        # Get related articles
        related_articles = Article.objects.filter(
            Q(category=article.category) | Q(tags__in=article.tags.all())
        ).exclude(id=article.id).distinct()[:3]
        
        context['related_articles'] = related_articles
        return context
