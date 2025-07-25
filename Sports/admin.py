from django.contrib import admin
from .models import Sport, Team, Player, Match

# Register your models here.
admin.site.register([Sport, Team, Player, Match])