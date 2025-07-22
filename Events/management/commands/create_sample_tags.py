from django.core.management.base import BaseCommand
from Events.models import EventTag
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Create sample event tags'

    def handle(self, *args, **options):
        tags_data = [
            {'name': 'Technology', 'color': '#007bff'},
            {'name': 'Health', 'color': '#28a745'},
            {'name': 'Education', 'color': '#6f42c1'},
            {'name': 'Business', 'color': '#fd7e14'},
            {'name': 'Arts', 'color': '#e83e8c'},
            {'name': 'Sports', 'color': '#20c997'},
            {'name': 'Music', 'color': '#6610f2'},
            {'name': 'Food', 'color': '#dc3545'},
            {'name': 'Environment', 'color': '#198754'},
            {'name': 'Community', 'color': '#0d6efd'},
        ]
        
        created_count = 0
        for tag_data in tags_data:
            tag, created = EventTag.objects.get_or_create(
                name=tag_data['name'],
                defaults={
                    'slug': slugify(tag_data['name']),
                    'color': tag_data['color']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f"Created tag: {tag.name}")
        
        if created_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {created_count} event tags!')
            )
        else:
            self.stdout.write(
                self.style.WARNING('All tags already exist.')
            )
