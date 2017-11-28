import urllib.request as ur
import texttable as tt
import json

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


table = tt.Texttable()
table.add_row(['Team', 'Score'])

for i in game_data:
    i = NflGame(i, game_data[i]['home']['abbr'], game_data[i]['away']['abbr'], game_data[i]['home']['score']['T'], game_data[i]['away']['score']['T'])
    table.add_row([i.home_team, i.home_score])
    table.add_row([i.away_team, i.away_score])

print(table.draw())
