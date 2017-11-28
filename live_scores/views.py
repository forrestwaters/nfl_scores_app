from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import urllib.request as ur
import json

def scores(request):
    current_weeks_games_url = 'http://www.nfl.com/liveupdate/scores/scores.json'

    # game_data will return a json array with live scores
    game_data = json.load(ur.urlopen(current_weeks_games_url))

    class NflGame:

        def __init__(self, gid, home_team, away_team, home_score, away_score):
            self.gid = gid
            self.home_team = home_team
            self.away_team = away_team
            self.home_score = home_score
            self.away_score = away_score
            self.game_url = 'http://www.nfl.com/liveupdate/game-center/' + self.gid + '/' + self.gid + '_gtd.json'

    html = '''<table>
    <thead>
        <style>
        td, th {
        border: 1px solid #999;
        padding: 0.5rem;
        }
        table {
        border-collapse: collapse;
        }
        </style>
        <tr>
            <th>Team</th>
            <th>Score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
'''

    # pass each game through the NflGame class so we have the attributes we're looking for
    for i in game_data:
        i = NflGame(i, game_data[i]['home']['abbr'], game_data[i]['away']['abbr'], game_data[i]['home']['score']['T'], game_data[i]['away']['score']['T'])
        html += '   <td>%s</td>' % i.home_team
        html += '   <td>%s</td>' % i.home_score
        html += '<tr>'
        html += '   <td>%s</td>' % i.away_team
        html += '   <td>%s</td>' % i.away_score
        html += '</tr>'

    html += '''
    </tbody>
</table>
            '''

    return HttpResponse(html)
