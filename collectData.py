import time
import grequests, requests
import pandas as pd
from datetime import timedelta, datetime
import threading
good_matches = []
headers = {
  'authority': 'api.sofascore.com',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
  'sec-ch-ua-mobile': '?1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
  'sec-ch-ua-platform': '"Android"',
  'accept': '*/*',
  'origin': 'https://www.sofascore.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.sofascore.com/',
  'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
  'if-none-match': 'W/"1eef0d3048"'
}
proxies={
        "http": "http://srcfqjix-rotate:cs09qwhxss11@p.webshare.io:80/",
        "https": "http://srcfqjix-rotate:cs09qwhxss11@p.webshare.io:80/"
    }
def get_data_day(date):
    """
    return a json object containing all the matches in "date" day
    """
    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}" # yyyy-mm-dd
    response = requests.get(url, headers=headers)
    print(response)
    return response.json()
def get_data_match(id):
    """
    return a json object containing all the statistics of a match, given its id
    """
    url_event = f"https://api.sofascore.com/api/v1/event/{id}"                  #0
    url_statistics = f"https://api.sofascore.com/api/v1/event/{id}/statistics"  #1
    url_lineups = f"https://api.sofascore.com/api/v1/event/{id}/lineups"        #2
    url_votes = f"https://api.sofascore.com/api/v1/event/{id}/votes"            #3
    url_form = f"https://api.sofascore.com/api/v1/event/{id}/pregame-form"      #4
    url_managers = f"https://api.sofascore.com/api/v1/event/{id}/managers"      #5
    event = requests.get(url_event, headers=headers).json()
    statistics = requests.get(url_statistics, headers=headers).json()["statistics"]

    print(id)
    match = {
        # event
        "tournament-name": event["event"]["tournament"]["name"],
        "country": event["event"]["tournament"]["category"]["name"],
        "round": event["event"]["roundInfo"]["round"],
        "city": event["event"]["venue"]["city"]["name"],
        "stadium": event["event"]["venue"]["stadium"]["name"],
        "referee": event["event"]["referee"]["name"],
        "home-team": event["event"]["homeTeam"]["name"],
        "home-team-id": event["event"]["homeTeam"]["id"],
        "away-team": event["event"]["awayTeam"]["name"],
        "away-team-id": event["event"]["awayTeam"]["id"],
        "home-score-period1": event["event"]["homeScore"]["period1"],
        "home-score": event["event"]["homeScore"]["current"],
        "away-score-period1": event["event"]["awayScore"]["period1"],
        "away-score": event["event"]["awayScore"]["current"],
        "hasGlobalHighlights": event["event"]["hasGlobalHighlights"],
        "hasEventPlayerStatistics": event["event"]["hasEventPlayerStatistics"],
        "hasEventPlayerHeatMap": event["event"]["hasEventPlayerHeatMap"],
        #statistics total
        "home_ball_possession": statistics[0]["groups"][0]["statisticsItems"][0]["home"],
        "away_ball_possession": statistics[0]["groups"][0]["statisticsItems"][0]["away"],
        "home_shots": statistics[0]["groups"][1]["statisticsItems"][0]["home"],
        "away_shots": statistics[0]["groups"][1]["statisticsItems"][0]["away"],
        "home_shots_on_target": statistics[0]["groups"][1]["statisticsItems"][1]["home"],
        "away_shots_on_target": statistics[0]["groups"][1]["statisticsItems"][1]["away"],
        "home_shots_off_target": statistics[0]["groups"][1]["statisticsItems"][2]["home"],
        "away_shots_off_target": statistics[0]["groups"][1]["statisticsItems"][2]["away"],
        "home_blocked_shots": statistics[0]["groups"][1]["statisticsItems"][3]["home"],
        "away_blocked_shots": statistics[0]["groups"][1]["statisticsItems"][3]["away"],
        "home_corner_kicks": statistics[0]["groups"][2]["statisticsItems"][0]["home"],
        "away_corner_kicks": statistics[0]["groups"][2]["statisticsItems"][0]["away"],
        "home_offsides": statistics[0]["groups"][2]["statisticsItems"][1]["home"],
        "away_offsides": statistics[0]["groups"][2]["statisticsItems"][1]["away"],
        "home_fouls": statistics[0]["groups"][2]["statisticsItems"][2]["home"],
        "away_fouls": statistics[0]["groups"][2]["statisticsItems"][2]["away"],
        "home_yellow_cards": statistics[0]["groups"][2]["statisticsItems"][3]["home"],
        "away_yellow_cards": statistics[0]["groups"][2]["statisticsItems"][3]["away"],
        "home_big_chances": statistics[0]["groups"][3]["statisticsItems"][0]["home"],
        "away_big_chances": statistics[0]["groups"][3]["statisticsItems"][0]["away"],
        "home_big_chances_missed": statistics[0]["groups"][3]["statisticsItems"][1]["home"],
        "away_big_chances_missed": statistics[0]["groups"][3]["statisticsItems"][1]["away"],
        "home_hit_woodwork": statistics[0]["groups"][3]["statisticsItems"][2]["home"],
        "away_hit_woodwork": statistics[0]["groups"][3]["statisticsItems"][2]["away"],
        "home_shots_inside_box": statistics[0]["groups"][3]["statisticsItems"][3]["home"],
        "away_shots_inside_box": statistics[0]["groups"][3]["statisticsItems"][3]["away"],
        "home_shots_outside_box": statistics[0]["groups"][3]["statisticsItems"][4]["home"],
        "away_shots_outside_box": statistics[0]["groups"][3]["statisticsItems"][4]["away"],
        "home_goalkeeper_saves": statistics[0]["groups"][3]["statisticsItems"][5]["home"],
        "away_goalkeeper_saves": statistics[0]["groups"][3]["statisticsItems"][5]["away"],
        "home_passes": statistics[0]["groups"][4]["statisticsItems"][0]["home"],
        "away_accurate_passes": statistics[0]["groups"][4]["statisticsItems"][0]["away"],
        "home_accurate_passes": statistics[0]["groups"][4]["statisticsItems"][1]["home"],
        "away_accurate_passes": statistics[0]["groups"][4]["statisticsItems"][1]["away"],
        "home_long_balls": statistics[0]["groups"][4]["statisticsItems"][2]["home"],
        "away_long_balls": statistics[0]["groups"][4]["statisticsItems"][2]["away"],
        "home_crosses": statistics[0]["groups"][4]["statisticsItems"][3]["home"],
        "away_crosses": statistics[0]["groups"][4]["statisticsItems"][3]["away"],
        "home_dribbles": statistics[0]["groups"][5]["statisticsItems"][0]["home"],
        "away_dribbles": statistics[0]["groups"][5]["statisticsItems"][0]["away"],
        "home_possesion_lost": statistics[0]["groups"][5]["statisticsItems"][1]["home"],
        "away_possesion_lost": statistics[0]["groups"][5]["statisticsItems"][1]["away"],
        "home_duels_won": statistics[0]["groups"][5]["statisticsItems"][2]["home"],
        "away_duels_won": statistics[0]["groups"][5]["statisticsItems"][2]["away"],
        "home_aerials_won": statistics[0]["groups"][5]["statisticsItems"][3]["home"],
        "away_aerials_won": statistics[0]["groups"][5]["statisticsItems"][3]["away"],
        "home_tackles": statistics[0]["groups"][6]["statisticsItems"][0]["home"],
        "away_tackles": statistics[0]["groups"][6]["statisticsItems"][0]["away"],
        "home_interceptions": statistics[0]["groups"][6]["statisticsItems"][1]["home"],
        "away_interceptions": statistics[0]["groups"][6]["statisticsItems"][1]["away"],
        "home_clearances": statistics[0]["groups"][6]["statisticsItems"][2]["home"],
        "away_clearances": statistics[0]["groups"][6]["statisticsItems"][2]["away"],
        #statistics 1 time
        "1ST_home_ball_possession": statistics[1]["groups"][0]["statisticsItems"][0]["home"],
        "1ST_away_ball_possession": statistics[1]["groups"][0]["statisticsItems"][0]["away"],
        "1ST_home_shots": statistics[1]["groups"][1]["statisticsItems"][0]["home"],
        "1ST_away_shots": statistics[1]["groups"][1]["statisticsItems"][0]["away"],
        "1ST_home_shots_on_target": statistics[1]["groups"][1]["statisticsItems"][1]["home"],
        "1ST_away_shots_on_target": statistics[1]["groups"][1]["statisticsItems"][1]["away"],
        "1ST_home_shots_off_target": statistics[1]["groups"][1]["statisticsItems"][2]["home"],
        "1ST_away_shots_off_target": statistics[1]["groups"][1]["statisticsItems"][2]["away"],
        "1ST_home_blocked_shots": statistics[1]["groups"][1]["statisticsItems"][3]["home"],
        "1ST_away_blocked_shots": statistics[1]["groups"][1]["statisticsItems"][3]["away"],
        "1ST_home_corner_kicks": statistics[1]["groups"][2]["statisticsItems"][0]["home"],
        "1ST_away_corner_kicks": statistics[1]["groups"][2]["statisticsItems"][0]["away"],
        "1ST_home_offsides": statistics[1]["groups"][2]["statisticsItems"][1]["home"],
        "1ST_away_offsides": statistics[1]["groups"][2]["statisticsItems"][1]["away"],
        "1ST_home_yellow_cards": statistics[1]["groups"][2]["statisticsItems"][2]["home"],
        "1ST_away_yellow_cards": statistics[1]["groups"][2]["statisticsItems"][2]["away"],
        "1ST_home_big_chances": statistics[1]["groups"][3]["statisticsItems"][0]["home"],
        "1ST_away_big_chances": statistics[1]["groups"][3]["statisticsItems"][0]["away"],
        "1ST_home_big_chances_missed": statistics[1]["groups"][3]["statisticsItems"][1]["home"],
        "1ST_away_big_chances_missed": statistics[1]["groups"][3]["statisticsItems"][1]["away"],
        "1ST_home_hit_woodwork": statistics[1]["groups"][3]["statisticsItems"][2]["home"],
        "1ST_away_hit_woodwork": statistics[1]["groups"][3]["statisticsItems"][2]["away"],
        "1ST_home_shots_inside_box": statistics[1]["groups"][3]["statisticsItems"][3]["home"],
        "1ST_away_shots_inside_box": statistics[1]["groups"][3]["statisticsItems"][3]["away"],
        "1ST_home_shots_outside_box": statistics[1]["groups"][3]["statisticsItems"][4]["home"],
        "1ST_away_shots_outside_box": statistics[1]["groups"][3]["statisticsItems"][4]["away"],
        "1ST_home_goalkeeper_saves": statistics[1]["groups"][3]["statisticsItems"][5]["home"],
        "1ST_away_goalkeeper_saves": statistics[1]["groups"][3]["statisticsItems"][5]["away"],
        "1ST_home_passes": statistics[1]["groups"][4]["statisticsItems"][0]["home"],
        "1ST_away_passes": statistics[1]["groups"][4]["statisticsItems"][0]["away"],
        "1ST_home_accurate_passes": statistics[1]["groups"][4]["statisticsItems"][1]["home"],
        "1ST_away_accurate_passes": statistics[1]["groups"][4]["statisticsItems"][1]["away"],
        "1ST_home_long_balls": statistics[1]["groups"][4]["statisticsItems"][2]["home"],
        "1ST_away_long_balls": statistics[1]["groups"][4]["statisticsItems"][2]["away"],
        "1ST_home_crosses": statistics[1]["groups"][4]["statisticsItems"][3]["home"],
        "1ST_away_crosses": statistics[1]["groups"][4]["statisticsItems"][3]["away"],
        "1ST_home_dribbles": statistics[1]["groups"][5]["statisticsItems"][0]["home"],
        "1ST_away_dribbles": statistics[1]["groups"][5]["statisticsItems"][0]["away"],
        "1ST_home_possesion_lost": statistics[1]["groups"][5]["statisticsItems"][1]["home"],
        "1ST_away_possesion_lost": statistics[1]["groups"][5]["statisticsItems"][1]["away"],
        "1ST_home_duels_won": statistics[1]["groups"][5]["statisticsItems"][2]["home"],
        "1ST_away_duels_won": statistics[1]["groups"][5]["statisticsItems"][2]["away"],
        "1ST_home_aerials_won": statistics[1]["groups"][5]["statisticsItems"][3]["home"],
        "1ST_away_aerials_won": statistics[1]["groups"][5]["statisticsItems"][3]["away"],
        "1ST_home_tackles": statistics[1]["groups"][6]["statisticsItems"][0]["home"],
        "1ST_away_tackles": statistics[1]["groups"][6]["statisticsItems"][0]["away"],
        "1ST_home_interceptions": statistics[1]["groups"][6]["statisticsItems"][1]["home"],
        "1ST_away_interceptions": statistics[1]["groups"][6]["statisticsItems"][1]["away"],
        "1ST_home_clearances": statistics[1]["groups"][6]["statisticsItems"][2]["home"],
        "1ST_away_clearances": statistics[1]["groups"][6]["statisticsItems"][2]["away"],
        # statistics 2 time
        "2ND_home_ball_possession": statistics[2]["groups"][0]["statisticsItems"][0]["home"],
        "2ND_away_ball_possession": statistics[2]["groups"][0]["statisticsItems"][0]["away"],
        "2ND_home_shots": statistics[2]["groups"][1]["statisticsItems"][0]["home"],
        "2ND_away_shots": statistics[2]["groups"][1]["statisticsItems"][0]["away"],
        "2ND_home_shots_on_target": statistics[2]["groups"][1]["statisticsItems"][1]["home"],
        "2ND_away_shots_on_target": statistics[2]["groups"][1]["statisticsItems"][1]["away"],
        "2ND_home_shots_off_target": statistics[2]["groups"][1]["statisticsItems"][2]["home"],
        "2ND_away_shots_off_target": statistics[2]["groups"][1]["statisticsItems"][2]["away"],
        "2ND_home_blocked_shots": statistics[2]["groups"][1]["statisticsItems"][3]["home"],
        "2ND_away_blocked_shots": statistics[2]["groups"][1]["statisticsItems"][3]["away"],
        "2ND_home_corner_kicks": statistics[2]["groups"][2]["statisticsItems"][0]["home"],
        "2ND_away_corner_kicks": statistics[2]["groups"][2]["statisticsItems"][0]["away"],
        "2ND_home_offsides": statistics[2]["groups"][2]["statisticsItems"][1]["home"],
        "2ND_away_offsides": statistics[2]["groups"][2]["statisticsItems"][1]["away"],
        "2ND_home_yellow_cards": statistics[2]["groups"][2]["statisticsItems"][2]["home"],
        "2ND_away_yellow_cards": statistics[2]["groups"][2]["statisticsItems"][2]["away"],
        "2ND_home_big_chances": statistics[2]["groups"][3]["statisticsItems"][0]["home"],
        "2ND_away_big_chances": statistics[2]["groups"][3]["statisticsItems"][0]["away"],
        "2ND_home_big_chances_missed": statistics[2]["groups"][3]["statisticsItems"][1]["home"],
        "2ND_away_big_chances_missed": statistics[2]["groups"][3]["statisticsItems"][1]["away"],
        "2ND_home_hit_woodwork": statistics[2]["groups"][3]["statisticsItems"][2]["home"],
        "2ND_away_hit_woodwork": statistics[2]["groups"][3]["statisticsItems"][2]["away"],
        "2ND_home_shots_inside_box": statistics[2]["groups"][3]["statisticsItems"][3]["home"],
        "2ND_away_shots_inside_box": statistics[2]["groups"][3]["statisticsItems"][3]["away"],
        "2ND_home_shots_outside_box": statistics[2]["groups"][3]["statisticsItems"][4]["home"],
        "2ND_away_shots_outside_box": statistics[2]["groups"][3]["statisticsItems"][4]["away"],
        "2ND_home_goalkeeper_saves": statistics[2]["groups"][3]["statisticsItems"][5]["home"],
        "2ND_away_goalkeeper_saves": statistics[2]["groups"][3]["statisticsItems"][5]["away"],
        "2ND_home_passes": statistics[2]["groups"][4]["statisticsItems"][0]["home"],
        "2ND_away_passes": statistics[2]["groups"][4]["statisticsItems"][0]["away"],
        "2ND_home_accurate_passes": statistics[2]["groups"][4]["statisticsItems"][1]["home"],
        "2ND_away_accurate_passes": statistics[2]["groups"][4]["statisticsItems"][1]["away"],
        "2ND_home_long_balls": statistics[2]["groups"][4]["statisticsItems"][2]["home"],
        "2ND_away_long_balls": statistics[2]["groups"][4]["statisticsItems"][2]["away"],
        "2ND_home_crosses": statistics[2]["groups"][4]["statisticsItems"][3]["home"],
        "2ND_away_crosses": statistics[2]["groups"][4]["statisticsItems"][3]["away"],
        "2ND_home_dribbles": statistics[2]["groups"][5]["statisticsItems"][0]["home"],
        "2ND_away_dribbles": statistics[2]["groups"][5]["statisticsItems"][0]["away"],
        "2ND_home_possesion_lost": statistics[2]["groups"][5]["statisticsItems"][1]["home"],
        "2ND_away_possesion_lost": statistics[2]["groups"][5]["statisticsItems"][1]["away"],
        "2ND_home_duels_won": statistics[2]["groups"][5]["statisticsItems"][2]["home"],
        "2ND_away_duels_won": statistics[2]["groups"][5]["statisticsItems"][2]["away"],
        "2ND_home_aerials_won": statistics[2]["groups"][5]["statisticsItems"][3]["home"],
        "2ND_away_aerials_won": statistics[2]["groups"][5]["statisticsItems"][3]["away"],
        "2ND_home_tackles": statistics[2]["groups"][6]["statisticsItems"][0]["home"],
        "2ND_away_tackles": statistics[2]["groups"][6]["statisticsItems"][0]["away"],
        "2ND_home_interceptions": statistics[2]["groups"][6]["statisticsItems"][1]["home"],
        "2ND_away_interceptions": statistics[2]["groups"][6]["statisticsItems"][1]["away"],
        "2ND_home_clearances": statistics[2]["groups"][6]["statisticsItems"][2]["home"],
        "2ND_away_clearances": statistics[2]["groups"][6]["statisticsItems"][2]["away"],
    }

    good_matches.append(match)
def get_all_data_matches_of_day(matches):
    threads = []
    for match in matches[:10]:
        t = threading.Thread(target=get_data_match, args=(match["id"],))
        t.start()
        threads.append(t)
    map(lambda t: t.join(), threads)
    while threads[-1].is_alive():
        #wait
        time.sleep(0.2)
if __name__ == '__main__':
    """startDate = datetime(2020,10,10)
    endDate = datetime(2020,10,11)
    dates = pd.date_range(startDate, endDate - timedelta(days=1), freq='d')
    for date in dates:
        date = date.strftime("%Y-%m-%d")
        while True:
            try:
                matches = get_data_day(date)
                break
            except Exception as E:
                print(E)
                print("Errore proxy")
        get_all_data_matches_of_day(matches["events"])
    df = pd.DataFrame(good_matches)
    df.to_csv("data.csv")"""
    get_data_match(9645192)
    df = pd.DataFrame(good_matches)
    df.to_csv("data.csv")