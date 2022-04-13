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

def rl_getPay():
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

def cs_getTeams():
    page = get_parsed_page("https://liquipedia.net/counterstrike/Portal:Teams")
    teams = []

    for team in page.find_all("span", {"class": ["team-template-text"], }):
        team = team.findChild().text
        teams.append(team)
    return teams

def cs_getTeamPay(team):
    page = get_parsed_page("https://liquipedia.net/counterstrike/" + team.replace(" ", "_"))
    results = page.find_all("div", {"class": ["infobox-cell-2"], })

    found = False
    for item in results[2:]:
        if found:
            return team + ": " + item.text
        if item.text == "Total Winnings:":
            found = True
    return "Not found"

def cs_getPay():
    #So very slow may need to find a different website
    #158 Active Teams // 631 Total Teams
    teams = cs_getTeams()[:158]
    combined = []

    for team in teams:
        combined.append(cs_getTeamPay(team))
    return combined

def d2_getPay():
    page = get_parsed_page("https://liquipedia.net/dota2/Portal:Statistics/Team_earnings")
    teams = []
    pay = []
    combined = []
    
    for team in page.find_all("span", {"class": ["team-template-text"], }):
        team = team.findChild().text
        teams.append(team)
        
    for team in page.find_all("span", {"class": ["team-template-team-standard"], }):
        team = team.parent.parent.findChildren()[15].text
        team = team[:-1]
        pay.append(team)

    count = 0
    for team in teams:
        combined.append(team + ": " + pay[count])
        count = count + 1
    return combined
    

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()

    pp.pprint(d2_getPay())
    
