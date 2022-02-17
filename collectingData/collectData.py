import time
import requests
import pandas as pd
from datetime import timedelta, datetime
import threading

good_matches = []

"""
UEFA Champions League
UEFA Europa League
Premier League
LaLiga
Bundesliga
Serie A
Ligue 1
Eredivise
Premiership (scozia)
Serie B
Pro League (belgio)
Superliga (danimarca)
Championship
Eliteserien
Lech pozann (polonia)
"""

top_tournament = [7,679,17,8,35,23,34,37,36,53,38,39,18,20,3121]

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
    url_incidents = f"https://api.sofascore.com/api/v1/event/{id}/incidents"

    try:
        event = requests.get(url_event, headers=headers).json()["event"]
    except:
        event = None

    try:
        statistics = requests.get(url_statistics, headers=headers).json()["statistics"]
    except:
        statistics = None

    try:
        lineups = requests.get(url_lineups, headers=headers).json()
    except:
        lineups = None

    try:
        votes = requests.get(url_votes, headers=headers).json()["vote"]
    except:
        votes = None

    try:
        form = requests.get(url_form, headers=headers).json()
    except:
        form = None

    try:
        managers = requests.get(url_managers, headers=headers).json()
    except:
        managers = None

    try:
        incidents = requests.get(url_incidents, headers=headers).json()["incidents"]
    except:
        incidents = None

    match = get_match_object(event, statistics, votes, form, managers, lineups, incidents)
    good_matches.append(match)

def get_match_object(event, statistics, votes, form, managers, lineups, incidents):
    match = {}

    # event
    try:
        match["timestamp"] = event["startTimestamp"],
    except Exception as e:
        print(e)
        match["timestamp"] = None

    try:
        match["tournament_name"] = event["tournament"]["name"],
    except Exception as e:
        print(e)
        match["tournament_name"] = None

    try:
        match["country"] = event["tournament"]["category"]["name"],
    except Exception as e:
        print(e)
        match["country"] = None

    try:
        match["round"] = event["roundInfo"]["round"],
    except Exception as e:
        print(e)
        match["round"] = None

    try:
        match["city"] = event["venue"]["city"]["name"],
    except Exception as e:
        print(e)
        match["city"] = None

    try:
        match["stadium"] = event["venue"]["stadium"]["name"],
    except Exception as e:
        print(e)
        match["stadium"] = None

    try:
        match["referee"] = event["referee"]["name"],
    except Exception as e:
        print(e)
        match["referee"] = None

    try:
        match["homeTeam"] = event["homeTeam"]["name"],
    except Exception as e:
        print(e)
        match["homeTeam"] = None

    try:
        match["homeTeam_id"] = event["homeTeam"]["id"],
    except Exception as e:
        print(e)
        match["homeTeam_id"] = None

    try:
        match["awayTeam"] = event["awayTeam"]["name"],
    except Exception as e:
        print(e)
        match["awayTeam"] = None

    try:
        match["awayTeam_id"] = event["awayTeam"]["id"],
    except Exception as e:
        print(e)
        match["awayTeam_id"] = None

    try:
        match["homeScore_period1"] = event["homeScore"]["period1"],
    except Exception as e:
        print(e)
        match["homeScore_period1"] = None

    try:
        match["homeScore"] = event["homeScore"]["current"],
    except Exception as e:
        print(e)
        match["homeScore"] = None

    try:
        match["awayScore_period1"] = event["awayScore"]["period1"],
    except Exception as e:
        print(e)
        match["awayScore_period1"] = None

    try:
        match["awayScore"] = event["awayScore"]["current"],
    except Exception as e:
        print(e)
        match["awayScore"] = None

    try:
        match["hasGlobalHighlights"] = event["hasGlobalHighlights"],
    except Exception as e:
        print(e)
        match["hasGlobalHighlights"] = None

    try:
        match["hasEventPlayerStatistics"] = event["hasEventPlayerStatistics"],
    except Exception as e:
        print(e)
        match["hasEventPlayerStatistics"] = None

    try:
        match["hasEventPlayerHeatMap"] = event["hasEventPlayerHeatMap"],
    except Exception as e:
        print(e)
        match["hasEventPlayerHeatMap"] = None

    # statistics
    try:
        for stat in statistics:
            for group in stat["groups"]:
                for item in group["statisticsItems"]:
                    match[f"{stat['period']}_{item['name']}_home".replace(" ", "_").lower()] = item["home"]
                    match[f"{stat['period']}_{item['name']}_away".replace(" ", "_").lower()] = item["away"]
    except Exception as e:
        print(e)


    # votes
    try:
        match["people_vote_1"] = votes['vote1']
    except Exception as e:
        print(e)
        match["people_vote_1"] = None

    try:
        match["people_vote_x"] = votes['voteX']
    except Exception as e:
        print(e)
        match["people_vote_x"] = None

    try:
        match["people_vote_2"] = votes['vote2']
    except Exception as e:
        print(e)
        match["people_vote_2"] = None

    # form
    try:
        match["homeTeam_avgRating"] = form["homeTeam"]["avgRating"]
    except Exception as e:
        print(e)
        match["homeTeam_avgRating"] = None

    try:
        match["homeTeam_position"] = form["homeTeam"]["position"]
    except Exception as e:
        print(e)
        match["homeTeam_position"] = None

    try:
        match["homeTeam_pts"] = form["homeTeam"]["value"]
    except Exception as e:
        print(e)
        match["homeTeam_pts"] = None

    try:
        match["homeTeam_form"] = form["homeTeam"]["form"]
    except Exception as e:
        print(e)
        match["homeTeam_form"] = None

    try:
        match["awayTeam_avgRating"] = form["awayTeam"]["avgRating"]
    except Exception as e:
        print(e)
        match["awayTeam_avgRating"] = None

    try:
        match["awayTeam_position"] = form["awayTeam"]["position"]
    except Exception as e:
        print(e)
        match["awayTeam_position"] = None

    try:
        match["awayTeam_pts"] = form["awayTeam"]["value"]
    except Exception as e:
        print(e)
        match["awayTeam_pts"] = None

    try:
        match["awayTeam_form"] = form["awayTeam"]["form"]
    except Exception as e:
        print(e)
        match["awayTeam_form"] = None


    # managers
    try:
        match["name_manager_home"] = managers["homeManager"]["name"]
    except Exception as e:
        print(e)
        match["name_manager_home"] = None

    try:
        match["id_manager_home"] = managers["homeManager"]["id"]
    except Exception as e:
        print(e)
        match["id_manager_home"] = None

    try:
        match["name_manager_away"] = managers["awayManager"]["name"]
    except Exception as e:
        print(e)
        match["name_manager_away"] = None

    try:
        match["id_manager_away"] = managers["awayManager"]["id"]
    except Exception as e:
        print(e)
        match["id_manager_away"] = None

    # lineups

    players = []
    for team in ["home", "away"]:
        players.append({f"{team}_formation": lineups[team]["formation"]})
        cont = 0
        for player in lineups[team]["players"]:
            try:
                if player["statistics"]:
                    cont += 1
                    players.append({f"{team}Player_{cont}_id": player["player"]["id"]})
                    players.append({f"{team}Player_{cont}_name": player["player"]["name"]})
                    players.append({f"{team}Player_{cont}_position": player["player"]["position"]})
                    for stat in player["statistics"]:
                        players.append({f"{team}Player_{cont}_{stat}": player["statistics"][stat]})
            except:
                print("ERROR PLAYER STATISTICS LINEUPS")
                continue

        cont = 0
        try:
            for player in lineups[team]["missingPlayers"]:
                try:
                    cont += 1
                    players.append({f"{team}MissingPlayer_{cont}_type": player["type"]})
                    players.append({f"{team}MissingPlayer_{cont}_id": player["player"]["id"]})
                    players.append({f"{team}MissingPlayer_{cont}_name": player["player"]["name"]})
                    players.append({f"{team}MissingPlayer_{cont}_position": player["player"]["position"]})
                except:
                    print("ERROR PLAYER STATISTICS LINEUPS")
                    continue
        except:
            print("NO MISSING PLAYERS")

    for x in players:
        key = list(x.keys())[0]
        value = x[key]
        match[key] = value

    # incidents
    match["penalty"] = 0
    match["varDecision"] = 0

    for incident in incidents:
        try:
            if incident["incidentClass"] == "penalty":
                match["penalty"] += 1
        except:
            pass
        if incident["incidentType"] == "varDecision":
            match["varDecision"] += 1

    return match

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
    startDate = datetime(2022,2,7)
    endDate = datetime(2022,2,7)
    dates = pd.date_range(startDate, endDate - timedelta(days=1), freq='d')
    for date in dates:
        print(date)
        date = date.strftime("%Y-%m-%d")
        matches = get_data_day(date)
        for match in matches["events"]:
            # check if the match is in a tournament
            try:
                if match["tournament"]["uniqueTournament"]["id"] in top_tournament:
                    get_data_match(match["id"])
            except Exception as e:
                print(["ERROR ID TOURNAMENT",match["id"], e])

        df = pd.DataFrame(good_matches)
        df.to_csv(f"data/{date}.csv")
        good_matches = []