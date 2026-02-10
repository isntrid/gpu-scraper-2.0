import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("strong")
mappings = {}
for tag in tags:
    if tag.getText().isdigit() and int(tag.getText()) >= 90: # need to fix so it can support >999 with commas 
        container = tag.find_parent("div", class_="item-cell")
        link_tag = container.find("a", class_="item-title")
        link = link_tag.get("href")
        name = link_tag.get_text()
        price = int(tag.get_text().strip())
        mappings[price] = [link, name]


cheapest_price = max(mappings.keys())
cheapest_link = mappings[cheapest_price][0]
cheapest_name = mappings[cheapest_price][1]
print(cheapest_link)
