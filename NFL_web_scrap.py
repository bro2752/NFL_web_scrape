import requests 
from bs4 import BeautifulSoup
#1. Make Git repo
#2. Create a virtual environment 
#3. Install Dependencies 

url = "https://www.nfl.com/stats/player-stats/"

#make requests to website
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

table_selector = "d3-o-table d3-o-table--detailed d3-o-player-stats--detailed d3-o-table--sortable"
player_div = soup.find("table", class_= table_selector)

player_selector = "d3-o-player-fullname nfl-o-cta--link"
name = soup.find("a", class_= player_selector)

print(name)