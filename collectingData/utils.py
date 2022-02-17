import requests
from datetime import datetime
import pandas as pd
from data.beans.Partita import Partita
import datetime

headers = {
  'authority': 'api.sofascore.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'accept': '*/*',
  'origin': 'https://www.sofascore.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.sofascore.com/',
  'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7'
}

proxies = {
    "http": "http://srcfqjix-rotate:cs09qwhxss11@p.webshare.io:80/",
    "https": "http://srcfqjix-rotate:cs09qwhxss11@p.webshare.io:80/"
}

top_tournament = [7,679,17,8,35,23,34,37,36,53,38,39,18,20,3121]

def get_match_data(id, side, side2):
    url_statistics = f"https://api.sofascore.com/api/v1/event/{id}/statistics"

    r = requests.get(url_statistics, headers=headers, proxies=proxies)
    stats = r.json()["statistics"][0]["groups"]

    statistics = {}
    no_stats = ["Accurate passes", "Long balls", "Crosses", "Dribbles"]
    for group in stats:
        for item in group["statisticsItems"]:
            if item["name"] not in no_stats:
                if side == 'home':
                    statistics[f"all_{item['name']}_{side2}".replace(" ", "_").lower()] = int(item["home"].replace("%",""))
                if side == 'away':
                    statistics[f"all_{item['name']}_{side2}".replace(" ", "_").lower()] = int(item["away"].replace("%",""))

    return statistics

def get_last_matches(id):
    url = f"https://api.sofascore.com/api/v1/team/{id}/events/last/0"
    r = requests.get(url, headers=headers)
    print(r)
    matches = r.json()["events"]

    ids = []
    cont = 0
    partite = 0
    while cont < 5:
        match = matches[len(matches) - partite - 1]
        print(match["status"])
        if match["status"]["type"] == "finished" and match["tournament"]["uniqueTournament"]["id"] in top_tournament:
            idHome = match["homeTeam"]["id"]
            idAway = match["awayTeam"]["id"]
            if id == idHome:
                ids.append((match["id"],"home"))
            elif id == idAway:
                ids.append((match["id"],"away"))
            cont += 1

        partite += 1

    return ids

def retrieveMatchByIdSofascore(id):
    url = f"https://api.sofascore.com/api/v1/event/{id}"
    match = requests.get(url, headers=headers, proxies=proxies).json()["event"]
    print(match)
    stats = {}

    url_votes = f"https://api.sofascore.com/api/v1/event/{id}/votes"
    r_votes = requests.get(url_votes, headers=headers, proxies=proxies)
    votes = r_votes.json()["vote"]
    print(votes)

    id = match["id"]
    home = match["homeTeam"]["name"]
    image_home = f"https://api.sofascore.app/api/v1/team/{match['homeTeam']['id']}/image"
    away = match["awayTeam"]["name"]
    away_image = f"https://api.sofascore.app/api/v1/team/{match['awayTeam']['id']}/image"
    tournament_name = match["tournament"]["name"]
    #date = datetime.utcfromtimestamp(int(match["startTimestamp"])).strftime('%Y-%m-%d')
    timestamp = int(match["startTimestamp"])

    stats["referee"] = match["referee"]["name"]
    stats["country"] = match["tournament"]["category"]["name"]
    stats["homeTeam_id"] = match["homeTeam"]["id"]
    stats["awayTeam_id"] = match["awayTeam"]["id"]
    stats["people_vote_1"] = int(votes["vote1"])
    stats["people_vote_x"] = int(votes["voteX"])
    stats["people_vote_2"] = int(votes["vote2"])

    lasts_home = get_last_matches(match["homeTeam"]["id"])
    lasts_away = get_last_matches(match["awayTeam"]["id"])

    home_stats = []
    print(f"partita {home} vs {away}")
    for home_match,homeOrAway in lasts_home:
        print(home_match, homeOrAway)
        home_stats.append(get_match_data(home_match,homeOrAway,"home" ))
    home_df = pd.DataFrame(home_stats)
    home_df = home_df[["all_ball_possession_home","all_shots_on_target_home","all_shots_off_target_home","all_corner_kicks_home","all_fouls_home","all_yellow_cards_home","all_goalkeeper_saves_home"]]


    away_stats = []
    for away_match,homeOrAway in lasts_away:
        print(away_match, homeOrAway)
        away_stats.append(get_match_data(away_match,homeOrAway,"away"))
    away_df = pd.DataFrame(away_stats)
    away_df = away_df[["all_ball_possession_away","all_shots_on_target_away","all_shots_off_target_away","all_corner_kicks_away","all_fouls_away","all_yellow_cards_away","all_goalkeeper_saves_away"]]

    home_df = pd.DataFrame(home_df.mean().to_dict(),index=[home_df.index.values[-1]])
    away_df = pd.DataFrame(away_df.mean().to_dict(), index=[away_df.index.values[-1]])

    home_df["id"] = id
    away_df["id"] = id

    df = pd.merge(home_df, away_df, on=["id"])

    partita = Partita(id, home, away, timestamp, tournament_name, image_home, away_image,
                    stats["referee"], stats["homeTeam_id"], stats["awayTeam_id"],stats["country"], df["all_fouls_home"][0],df["all_fouls_away"][0], df["all_yellow_cards_home"][0], df["all_yellow_cards_away"][0],
                    df["all_ball_possession_away"][0], df["all_shots_on_target_home"][0], df["all_shots_off_target_home"][0],
                    df["all_corner_kicks_home"][0], df["all_corner_kicks_away"][0], df["all_goalkeeper_saves_away"][0],
                    stats["people_vote_x"], stats["people_vote_2"])

    return partita

def retrieveMatchesByDateSofascore(date):
    #date format "2022-02-16"

    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}"
    r = requests.get(url, headers=headers, proxies=proxies)
    matches = r.json()["events"]

    element = datetime.datetime.strptime(date, "%Y-%m-%d")

    timestamp = datetime.datetime.timestamp(element)

    goods = []
    for match in matches:
        # only our leagues
        try:
            if match["tournament"]["uniqueTournament"]["id"] in top_tournament and int(match["startTimestamp"]) > timestamp :
                id = match["id"]
                goods.append(id)
        except:
            pass

    return goods