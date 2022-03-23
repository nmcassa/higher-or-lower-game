import re
import requests
import datetime
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    # This fixes a blocked by cloudflare error i've encountered
    headers = {
        "referer": "https://liquipedia.net/rocketleague/Portal:Statistics",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

def getPay():
    page = get_parsed_page("https://liquipedia.net/rocketleague/Portal:Statistics")
    
    teams = []
    pay = []
    combined = []
    
    for team in page.find_all("span", {"class": ["team-template-text"], }):
        team = team.findChild().text   
        teams.append(team)

    for team in page.find_all("span", {"class": ["team-template-team-standard"], }):
        p = team.parent.parent
        children = p.findChildren("td")
        pay.append(children[5].text)

    count = 0
    for team in teams:
        combined.append(team + ": " + pay[count])
        count += 1
        
    return combined

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()
    
    pp.pprint(getPay())
    
