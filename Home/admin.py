from django.contrib import admin
from .models import LandingFeature

# Register your models here.
@admin.register(LandingFeature)
class LandingFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'is_active', 'priority', 'created_at')
    list_filter = ('section', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'priority')
    ordering = ('section', 'priority')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'image')
        }),
        ('Settings', {
            'fields': ('section', 'link', 'is_active', 'priority')
        }),
    )
