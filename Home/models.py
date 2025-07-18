from django.db import models
from django.utils import timezone

class LandingFeature(models.Model):
    SECTION_CHOICES = [
        ('news', 'News'),
        ('sports', 'Sports'),
        ('events', 'Events'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='landing_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    is_active = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['priority']
        verbose_name = "Landing Page Feature"
        verbose_name_plural = "Landing Page Features"

    def __str__(self):
        return f"{self.get_section_display()} - {self.title}"
    
    @property
    def related_features(self):
        """Return other active features in the same section, excluding self"""
        return LandingFeature.objects.filter(
            section=self.section, 
            is_active=True
        ).exclude(id=self.id)


