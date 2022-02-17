from datetime import datetime
import requests
from data.beans.Partita import Partita

headers = {
  'authority': 'api.sofascore.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'accept': '/',
  'origin': 'https://www.sofascore.com/',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.sofascore.com/',
  'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7'
}

proxies = {
    "http": "http://p.webshare.io:80/",
    "https": "http://p.webshare.io:80/"
}

top_tournament = [7,679,17,8,35,23,34,37,36,53,38,39,18,20,3121]

def retrieveMatchesByDate(date):
    #date format "2022-02-16"

    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/%7Bdate%7D"
    r = requests.get(url, headers=headers, proxies=proxies)
    matches = r.json()["events"]

    goods = []
    for match in matches:
        # only our leagues
        try:
            if match["tournament"]["uniqueTournament"]["id"] in top_tournament:
                id = match["id"]
                home = match["homeTeam"]["name"]
                image_home = f"https://api.sofascore.app/api/v1/team/%7Bmatch[%27homeTeam%27][%27id%27]%7D/image"
                away = match["awayTeam"]["name"]
                away_image = f"https://api.sofascore.app/api/v1/team/%7Bmatch[%27awayTeam%27][%27id%27]%7D/image"
                league = match["tournament"]["name"]
                date = datetime.utcfromtimestamp(int(match["startTimestamp"])).strftime('%Y-%m-%d')

                #id, nomeCasa, nomeFuoriCasa, dataIncontro, league, home_image, away_image
                partita = Partita(id, home, away, date, league, image_home, away_image, None, None)
                goods.append(partita)
        except:
            pass

    return goods

def retrieveMatchById(id):
    # TODO
    pass