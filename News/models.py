from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news:category_detail', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news:tag_detail', args=[self.slug])


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('featured', 'Featured'),
        ('archived', 'Archived')
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    
    featured_image = models.ImageField(upload_to='news_images/%Y/%m/%d/', blank=True, null=True)
    excerpt = models.TextField(blank=True, max_length=500)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-publish_date']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news:article_detail', args=[
            self.publish_date.year,
            self.publish_date.month,
            self.publish_date.day,
            self.slug
        ])
    
    def get_featured_image_url(self):
        """Return the featured image URL if it exists, otherwise return a placeholder."""
        if self.featured_image and hasattr(self.featured_image, 'url'):
            try:
                return self.featured_image.url
            except ValueError:
                # Image file doesn't exist
                return 'https://via.placeholder.com/800x400/1e3c72/ffffff?text=News+Article'
        return 'https://via.placeholder.com/800x400/1e3c72/ffffff?text=News+Article'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f'Comment by {self.name} on {self.article}'
    
    def get_replies(self):
        return Comment.objects.filter(parent=self).filter(active=True)
    
    @property
    def is_parent(self):
        return self.parent is None
