from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

def get_dummy_sports():
    """Return a list of dummy sports categories that can be used by views."""
    return [
        {
            'name': 'Football',
            'pk': 1,
            'image': {'url': 'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?q=80&w=2070&auto=format&fit=crop'},
            'description': 'The world\'s most popular sport played with a spherical ball between two teams of eleven players.'
        },
        {
            'name': 'Basketball',
            'pk': 2,
            'image': {'url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?q=80&w=2090&auto=format&fit=crop'},
            'description': 'A team sport in which two teams of five players compete to score points by throwing a ball through a hoop.'
        },
        {
            'name': 'Tennis',
            'pk': 3,
            'image': {'url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?q=80&w=2018&auto=format&fit=crop'},
            'description': 'A racket sport played individually or between two teams of two players each.'
        },
        {
            'name': 'Cricket',
            'pk': 4,
            'image': {'url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?q=80&w=2005&auto=format&fit=crop'},
            'description': 'A bat-and-ball game played between two teams of eleven players on a field with a wicket at each end.'
        },
        {
            'name': 'Rugby',
            'pk': 5,
            'image': {'url': 'https://images.unsplash.com/photo-1544943910-4c1dc44aab44?q=80&w=2062&auto=format&fit=crop'},
            'description': 'A team sport played with an oval ball that may be kicked, carried, and passed from hand to hand.'
        },
        {
            'name': 'Golf',
            'pk': 6,
            'image': {'url': 'https://images.unsplash.com/photo-1535131749006-b7f58c99034b?q=80&w=2070&auto=format&fit=crop'},
            'description': 'A precision club-and-ball sport in which players use various clubs to hit balls into holes on a course.'
        },
        {
            'name': 'Swimming',
            'pk': 7,
            'image': {'url': 'https://images.unsplash.com/photo-1530549387789-4c1017266635?q=80&w=2070&auto=format&fit=crop'},
            'description': 'A sport that involves propelling the body through water using the arms and legs.'
        },
        {
            'name': 'Athletics',
            'pk': 8,
            'image': {'url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=2070&auto=format&fit=crop'},
            'description': 'A collection of sporting events that involve competitive running, jumping, throwing, and walking.'
        },
        {
            'name': 'Volleyball',
            'pk': 9,
            'image': {'url': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?q=80&w=2007&auto=format&fit=crop'},
            'description': 'A team sport in which two teams of six players are separated by a net.'
        }
    ]

def team_detail(request, pk):
    return render(request, 'Sports/team_detail.html', {'team': {
        'name': 'Team Name',
        'sport': {'name': 'Sport Name'},
        'description': 'Team description goes here'
    }})

def player_detail(request, pk):
    return render(request, 'Sports/player_detail.html', {'player': {
        'first_name': 'John',
        'last_name': 'Doe',
        'team': {'name': 'Team Name'},
        'position': 'Forward',
        'jersey_number': 10,
        'bio': 'Player bio goes here'
    }})

def match_detail(request, pk):
    return render(request, 'Sports/match_detail.html', {'match': {
        'home_team': {'name': 'Home Team'},
        'away_team': {'name': 'Away Team'},
        'match_date': '2025-07-28',
        'venue': 'Stadium Name',
        'status': 'scheduled',
        'summary': 'Match summary goes here'
    }})

def article_detail(request, sport):
    article = ARTICLE_DATA.get(sport)
    if not article:
        raise Http404("Article not found")
    return render(request, 'Sports/article_detail.html', {
        'image_url': article['image_url'],
        'sport': article['sport'],
        'headline': article['headline'],
        'article': article['article'],
    })

def sport_detail(request, pk):
    sports = get_dummy_sports()
    sport = next((s for s in sports if s['pk'] == int(pk)), None)
    if not sport:
        raise Http404("Sport not found")
    return render(request, 'Sports/sport_detail.html', {'sport': sport})

def sport_list(request):
    sports = get_dummy_sports()
    for sport in sports:
        article = ARTICLE_DATA.get(sport['name'].lower())
        if article:
            sport['image_url'] = article['image_url']
    return render(request, 'Sports/sport_list.html', {'sports': sports})

ARTICLE_DATA = {
    
    'basketball': {
        'sport': 'Basketball',
        'headline': 'NBA 2K26 All-Summer League teams announced.',
        'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?q=80&w=2090&auto=format&fit=crop',
        'article': '''<ul>
<li>NBA Standings:Kyle Filipowski</li>
<li>Next Big Game: Oklahoma City Thunder vs. Indiana Pacers</li>
<li>Top Scorer: Nique Clifford</li>
<li>Full Article: The NBA has announced the NBA 2K26 All-Summer League teams, along with the NBA 2K26 All-Summer League Most Valuable Player. NBA 2K26 Summer League wrapped up on Sunday night with the Charlotte Hornets defeating the Kings in the championship game.

</li>
</ul>''',
    },
    'wrestling': {
        'sport': 'Wrestling',
        'headline': 'Revealed: What killed wrestling legend Hulk Hogan.',
        'image_url': 'https://www.tv47.digital/wp-content/uploads/2025/07/Hosts-Morocco-secured-a-dramatic-4-2-victory-over-the-Democratic-Republic-of-Congo-in-a-pulsating-Group-A-encounter-of-the-TotalEnergies-CAF-Womens-Africa-Cup-of-Nations-Morocco-2024-on-Wednesday-6-1.jpg',
        'article': '''<ul>
<li>Grand Slam: Wimbledon 2025</li>
<li>Top Seed: Iga Swiatek</li>
<li>Latest Winner: Novak Djokovic</li>
<li>Full Article: Serena’s comeback is highly anticipated, with fans eager to see her performance against the world’s best.</li>
</ul>''',
    },
    'volleyball': {
        'sport': 'Volleyball',
        'headline': "In-form Kamara dropped as Tarus names team for Africa Nations Championship.",
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthP2UKZ0IhZQq4OAXnSNBAETiO8kcBXKGL3hLF6Tgu33bZ8roRCxlS06n5F4yn6DWkBc&usqp=CAU',
        'article': '''<ul>
<li>African Championship: Kenya vs Egypt in the finals</li>
<li>Top Player: Simon Kipkorir
</li>
<li>Next Tournament: World Cup Qualifiers</li>
<li>Full Article: The national men’s volleyball team head coach Gideon Tarus has named his final 14-member team ahead of next week's African Nations Championship in Kigali, Rwanda.

The team which is set to depart today (Sunday) for host nation ahead of the event slated for September 5 to 15 will be without experienced Kenya Prisons attacker Michael Chemos, Kenya Defence Forces duo of Bernard Wechuli and Aggrey Kibungei as well Prisons Meshack Wambua</li>
</ul>''',
    },
    'rugby': {
        'sport': 'Rugby',
        'headline': 'The Rugby World Cup qualifiers heat up as top teams battle for a spot in the tournament.',
        'image_url': 'https://eu-cdn.rugbypass.com/webp-images/wp/wp-content/uploads/2024/11/All-Blacks-Italy-2024-1024x576.jpg.webp?maxw=766&comp=95',
        'article': '''<ul>
<li>World Cup Qualifiers: South Africa, New Zealand, England</li>
<li>Next Big Match: South Africa vs New Zealand</li>
<li>Top Try Scorer:  Harry Wilson</li>
<li>Full Article: After a last-gasp win over the Flying Fijians in Newcastle earlier this month, the Wallabies turned their focus towards the Lions Series opener in the River City. The Lions went into the match as strong favourites, and the visitors lived up to that label in the first Test.

Sione Tuipulotu and Tom Curry scored a try each as the Lions took control during the opening 40 minutes, before Dan Sheehan crossed early in the second term to extend their lead to a commanding 24-5 margin by the 42nd minute.</li>
</ul>''',
    },
    'tennis': {
        'sport': 'Wrestling',
        'headline': 'Revealed: What killed wrestling legend Hulk Hogan.',
        'image_url': 'https://www.tv47.digital/wp-content/uploads/2025/07/Hosts-Morocco-secured-a-dramatic-4-2-victory-over-the-Democratic-Republic-of-Congo-in-a-pulsating-Group-A-encounter-of-the-TotalEnergies-CAF-Womens-Africa-Cup-of-Nations-Morocco-2024-on-Wednesday-6-1.jpg',
        'article': '''<ul>
<li>Grand Slam: Two-time WWE Hall of Famer and former world champion</li>
<li>Top Seed:WWE achieve global recognition in the 1980s.</li>
<li>Latest Winner: WWE Hall of Famer and former world champion</li>
<li>Full Article: The professional wrestling world and its legions of fans across the globe are mourning the unexpected death of Terry Bollea, universally known as Hulk Hogan, who passed away on Thursday at the age of 71. The cause of death has been confirmed as cardiac arrest.

The news of Hogan’s sudden demise sent shockwaves through the sports entertainment community. Emergency responders were dispatched to Hogan’s residence in Clearwater, Florida, on Thursday morning following a 911 call reporting a possible cardiac arrest..</li>
</ul>''',
    },
    'football': {
        'sport': 'Football',
        'headline': 'Manchester City clinched a dramatic win over Arsenal in a thrilling Premier League encounter last night.',
        'image_url': 'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?q=80&w=2070&auto=format&fit=crop',
        'article': '''<ul>
<li>Premier League Standings: Brentford v Chelsea</li>
<li>Next Big Match: Man City v Burnley</li>
<li>Top Scorer: Erling Haaland</li>
<li>Full Article: The broadcast selections have been announced for live TV in the UK for Premier League matches in Matchweeks 4, 5 and 6 in September.

While the Premier League's fixture announcement dates advised that September's fixtures would be released on 9 July, delays in local approvals for fixtures unfortunately meant only August fixtures were announced on this date.

The Premier League would like to apologise for not being able to confirm these fixtures until now. However, today's announcement is in line with our commitment to give at least six weeks' notice for fixture announcements before January. 

All kick-off times are 15:00 BST unless otherwise mentioned. 

</li>
</ul>''',
    },
}
