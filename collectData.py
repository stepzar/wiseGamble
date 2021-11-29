import requests
import ast
from bs4 import BeautifulSoup

headers = {
  'authority': 'it.whoscored.com',
  'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
  'accept': 'text/plain, */*; q=0.01',
  'model-last-mode': 'JGH9VQUv+2vTgU+gJw7WE98xJirNpno32TFbicL0G8A=',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://it.whoscored.com/LiveScores',
  'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'visid_incap_774906=tc5WFaRBQwWTfKSFgUx14Yrpm2EAAAAAQUIPAAAAAACKKoDzhlKocr7OVujuvaLg; selection=null; incap_ses_478_774906=0pwJYek3Dg07O2t49TKiBvYxpWEAAAAA5oPLcLIRUBTmr6AAdoNUoA==; incap_ses_478_774906=5osvDOagiw03UWx49TKiBtoypWEAAAAAcUW7Z5B53RcnhtlaPR45VA=='
}

proxies={
        "http": "http://ifmxynlu-rotate:9awh3bms4ovl@p.webshare.io:80/",
        "https": "http://ifmxynlu-rotate:9awh3bms4ovl@p.webshare.io:80/"
    }

def get_data_day(data):
    url = f"https://it.whoscored.com/matchesfeed/?d={data}"
    response = requests.get(url, headers=headers, proxies=proxies)

    return ast.literal_eval(response.text.replace(",,,",",").replace(",,",","))[2]


def get_data_match(id):
    url = f"https://it.whoscored.com/Matches/{id}"
    response = requests.get(url, headers=headers)

    return response.text

def get_match_object(html):
    print(html)
    soup = BeautifulSoup(html, "lxml")
    home = soup.find("span", {"class":"col12-lg-4 col12-m-4 col12-s-0 col12-xs-0 home team"}).text
    print(home)

if __name__ == '__main__':
    """matches = get_data_day("20211128")
    for match in matches:"""

    html = get_data_match("1575905")
    get_match_object(html)


