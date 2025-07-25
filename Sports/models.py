from django.db import models
from django.utils import timezone

class Sport(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sports/images/', null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Sport"
        verbose_name_plural = "Sports"

class Team(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='teams')
    logo = models.ImageField(upload_to='teams/logos/', null=True, blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sport.name})"

    class Meta:
        ordering = ['name']
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    jersey_number = models.PositiveIntegerField()
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='players/photos/', null=True, blank=True)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = timezone.now().date()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Player"
        verbose_name_plural = "Players"

class Match(models.Model):
    MATCH_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('live', 'Live'),
        ('completed', 'Completed'),
        ('postponed', 'Postponed'),
        ('cancelled', 'Cancelled'),
    ]

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=MATCH_STATUS_CHOICES, default='scheduled')
    home_score = models.PositiveIntegerField(null=True, blank=True)
    away_score = models.PositiveIntegerField(null=True, blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.match_date.date()}"

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['-match_date']