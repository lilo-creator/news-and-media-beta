from django.core.management.base import BaseCommand
from Sports.models import Sport

class Command(BaseCommand):
    help = 'Create sample sports data'

    def handle(self, *args, **options):
        sports_data = [
            {
                'name': 'Football',
                'description': 'A team sport played between two teams of eleven players with a spherical ball.',
            },
            {
                'name': 'Basketball',
                'description': 'A team sport in which two teams, most commonly of five players each, oppose each other on a rectangular court.',
            },
            {
                'name': 'Tennis',
                'description': 'A racket sport that can be played individually against a single opponent or between two teams of two players each.',
            },
            {
                'name': 'Volleyball',
                'description': 'A team sport in which two teams of six players are separated by a net.',
            },
            {
                'name': 'Rugby',
                'description': 'A team sport played with an oval-shaped ball by two teams of 15 players.',
            },
        ]

        for sport in sports_data:
            obj, created = Sport.objects.get_or_create(name=sport['name'], defaults={'description': sport['description']})
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created sport: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Sport already exists: {obj.name}"))
