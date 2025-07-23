from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

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
    thumbnail = models.ImageField(upload_to='news_thumbnails/%Y/%m/%d/', blank=True, null=True)
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

    featured = models.BooleanField(default=False, help_text="Display this article on the home page")
    reading_time = models.PositiveIntegerField(default=0, help_text="Estimated reading time in minutes")
    likes_count = models.PositiveIntegerField(default=0)
    share_count = models.PositiveIntegerField(default=0)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_featured = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-publish_date']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news:article_detail', args=[
            self.publish_date.year,
            self.publish_date.strftime('%m'),
            self.publish_date.strftime('%d'),
            self.slug
        ])
    
    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])

    def increment_likes(self):
        self.likes_count += 1
        self.save(update_fields=['likes_count'])

    def increment_shares(self):
        self.share_count += 1
        self.save(update_fields=['share_count'])

    def calculate_reading_time(self):
        words_per_minute = 200
        word_count = len(self.content.split())
        self.reading_time = max(1, round(word_count / words_per_minute))
        return self.reading_time

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.reading_time:
            self.calculate_reading_time()
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    reported = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
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
