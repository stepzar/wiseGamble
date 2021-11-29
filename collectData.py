import requests
import json

headers = {
    'authority': 'es-ds.enetscores.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.enetscores.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.enetscores.com/',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
}

def get_data_day(data):
    url = f"https://es-ds.enetscores.com/4.571/FWB14705F6C8937012/live-en-livescore-daily-1-{data}-p0100-cid_0"
    response = requests(url, headers=headers)

    return json.loads(response.json()["content"])

def get_data_match(id):
    url = f"https://es-ds.enetscores.com/4.571/FWB14705F6C8937012/live-en-event-incidents-1-{id}-t_g"
    response = requests.get(url, headers=headers)

    return json.loads(response.json()["content"])

if __name__ == '__main__':
    x = get_data_day("20211128")
    with open('giorno.json', 'w') as f:
        json.dump(x, f)

    x = get_data_day("3657129")
    with open('partita.json', 'w') as f:
        json.dump(x, f)