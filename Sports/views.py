
from django.shortcuts import render, get_object_or_404
from .models import Sport, Team, Player, Match
from itertools import chain

# List all sports
def sport_list(request):
    sports = Sport.objects.all()
    return render(request, 'Sports/sport_list.html', {'sports': sports})

# Sport detail with teams
def sport_detail(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    return render(request, 'Sports/sport_detail.html', {'sport': sport})

# Team detail with players and matches
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    home_matches = team.home_matches.all()
    away_matches = team.away_matches.all()
    matches = list(chain(home_matches, away_matches))
    return render(request, 'Sports/team_detail.html', {'team': team, 'matches': matches})

# Player detail
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'Sports/player_detail.html', {'player': player})

# Match detail
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'Sports/match_detail.html', {'match': match})
