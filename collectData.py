import time
import requests
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
    url_event = f"https://api.sofascore.com/api/v1/event/{id}"
    url_statistics = f"https://api.sofascore.com/api/v1/event/{id}/statistics"
    url_lineups = f"https://api.sofascore.com/api/v1/event/{id}/lineups"
    url_votes = f"https://api.sofascore.com/api/v1/event/{id}/votes"
    url_form = f"https://api.sofascore.com/api/v1/event/{id}/pregame-form"
    url_managers = f"https://api.sofascore.com/api/v1/event/{id}/managers"
    event = requests.get(url_event, headers=headers).json()["event"]
    statistics = requests.get(url_statistics, headers=headers).json()["statistics"]
    lineups = requests.get(url_lineups, headers=headers).json()

    print(id)
    match = get_match_object(event, statistics)
    match_lineups = get_match_lineups(lineups)
    good_matches.append(match)

def get_match_object(event, statistics):
    match = {}

    # event
    match["tournament_name"] = event["tournament"]["name"],
    match["country"] = event["tournament"]["category"]["name"],
    match["round"] = event["roundInfo"]["round"],
    match["city"] = event["venue"]["city"]["name"],
    match["stadium"] = event["venue"]["stadium"]["name"],
    match["referee"] = event["referee"]["name"],
    match["homeTeam"] = event["homeTeam"]["name"],
    match["homeTeam_id"] = event["homeTeam"]["id"],
    match["awayTeam"] = event["awayTeam"]["name"],
    match["awayTeam_id"] = event["awayTeam"]["id"],
    match["homeScore_period1"] = event["homeScore"]["period1"],
    match["homeScore"] = event["homeScore"]["current"],
    match["awayScore_period1"] = event["awayScore"]["period1"],
    match["awayScore"] = event["awayScore"]["current"],
    match["hasGlobalHighlights"] = event["hasGlobalHighlights"],
    match["hasEventPlayerStatistics"] = event["hasEventPlayerStatistics"],
    match["hasEventPlayerHeatMap"] = event["hasEventPlayerHeatMap"],

    # statistics
    for stat in statistics:
        for group in stat["groups"]:
            for item in group["statisticsItems"]:
                match[f"{stat['period']}_{item['name']}_home".replace(" ", "_").lower()] = item["home"]
                match[f"{stat['period']}_{item['name']}_away".replace(" ", "_").lower()] = item["away"]
                #print(item)

    return match

def get_match_lineups(lineups):
    match_lineups = {}

    #lineups (formation, modul, players unavailable, players statistics match)

    #home lineups
    home = lineups["home"]
    players_home = home["players"]
    i = 0
    for player in players_home:
        match_lineups[f"id_player{i}_home"] = player["player"]["id"]
        match_lineups[f"name_player{i}_home"] = player["player"]["name"]
        match_lineups[f"position_player{i}_home"] = player["position"]
        match_lineups[f"shirtNumber_player{i}_home"] = player["shirtNumber"]
        match_lineups[f"position_player{i}_home"] = player["position"]
        i = i+1
        #the scraping of the "statistics" array is missing
        #"statistics" array is empty for players who have NOT played
    match_lineups["formation_module_home"] = home["formation"]
    missing_players_home = home["missingPlayers"]
    i = 0
    for player in missing_players_home:
        match_lineups[f"type_player_missing{i}_home"] = player["type"]
        match_lineups[f"id_player_missing{i}_home"] = player["player"]["id"]
        match_lineups[f"name_player_missing{i}_home"] = player["player"]["name"]
        match_lineups[f"position_player_missing{i}_home"] = player["player"]["position"]
        i = i + 1

    #away lineups
    away = lineups["away"]
    players_away = away["players"]
    i = 0
    for player in players_away:
        match_lineups[f"id_player{i}_away"] = player["player"]["id"]
        match_lineups[f"name_player{i}_away"] = player["player"]["name"]
        match_lineups[f"position_player{i}_away"] = player["position"]
        match_lineups[f"shirtNumber_player{i}_away"] = player["shirtNumber"]
        match_lineups[f"position_player{i}_away"] = player["position"]
        i = i+1
        # the scraping of the "statistics" array is missing
        # "statistics" array is empty for players who have NOT played
    match_lineups["formation_module_away"] = home["formation"]
    missing_players_away = away["missingPlayers"]
    i = 0
    for player in missing_players_away:
        match_lineups[f"type_player_missing{i}_away"] = player["type"]
        match_lineups[f"id_player_missing{i}_away"] = player["player"]["id"]
        match_lineups[f"name_player_missing{i}_away"] = player["player"]["name"]
        match_lineups[f"position_player_missing{i}_away"] = player["player"]["position"]
        i = i + 1

    print(match_lineups)
    return match_lineups

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
    """
    startDate = datetime(2020,10,10)
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
    df.to_csv("data.csv")
    """

    get_data_match(9645192)
    df = pd.DataFrame(good_matches)
    df.to_csv("data.csv")