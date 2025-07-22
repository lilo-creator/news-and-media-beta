from django.contrib import admin
from .models import Event, EventHost, EventTag, EventHighlight, EventRegistration

class EventHighlightInline(admin.TabularInline):
    model = EventHighlight
    extra = 1

@admin.register(EventHost)
class EventHostAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'created_at')
    search_fields = ('name', 'contact_email')
    list_filter = ('created_at',)

@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue_name', 'host', 'is_featured', 'is_active', 'views_count')
    list_filter = ('date', 'is_featured', 'is_active', 'host', 'tags')
    search_fields = ('title', 'description', 'venue_name')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    inlines = [EventHighlightInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'host')
        }),
        ('Date & Time', {
            'fields': ('date', 'start_time', 'end_time')
        }),
        ('Location', {
            'fields': ('venue_name', 'venue_address')
        }),
        ('Media', {
            'fields': ('banner_image', 'banner_image_url')
        }),
        ('Ticket Information', {
            'fields': ('ticket_price', 'registration_link')
        }),
        ('Settings', {
            'fields': ('tags', 'is_featured', 'is_active')
        }),
    )

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'registered_at')
    list_filter = ('event', 'registered_at')
    search_fields = ('name', 'email', 'event__title')
    readonly_fields = ('registered_at',)
