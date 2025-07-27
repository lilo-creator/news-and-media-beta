from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class EventHost(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='event_hosts/', blank=True, null=True)
    logo_url = models.URLField(blank=True)
    contact_email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class EventTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff')  # Hex color code
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    
    # Date and Time
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    # Location
    venue_name = models.CharField(max_length=200)
    venue_address = models.TextField()
    
    # Host Information
    host = models.ForeignKey(EventHost, on_delete=models.CASCADE, related_name='events')
    
    # Media
    banner_image = models.ImageField(upload_to='event_banners/%Y/%m/', blank=True, null=True)
    banner_image_url = models.URLField(blank=True)
    
    # Ticket Information
    ticket_price = models.CharField(max_length=100, default='Free Entry')
    registration_link = models.URLField(blank=True)
    
    # Relations
    tags = models.ManyToManyField(EventTag, blank=True, related_name='events')
    
    # Meta
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-date', '-start_time']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.slug])
    
    def get_banner_image_url(self):
        """Return the banner image URL if it exists, otherwise return a placeholder."""
        if self.banner_image and hasattr(self.banner_image, 'url'):
            try:
                return self.banner_image.url
            except ValueError:
                # Image file doesn't exist
                return 'https://via.placeholder.com/1200x600/667eea/ffffff?text=Event'
        elif self.banner_image_url:
            return self.banner_image_url
        return 'https://via.placeholder.com/1200x600/667eea/ffffff?text=Event'
    
    @property
    def is_upcoming(self):
        return self.date >= timezone.now().date()
    
    @property
    def time_display(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"
    
    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])


class EventHighlight(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # For Font Awesome or Bootstrap icons
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
        
    def __str__(self):
        return f"{self.event.title} - {self.title}"


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-registered_at']
        unique_together = ['event', 'email']
        
    def __str__(self):
        return f"{self.name} - {self.event.title}"
