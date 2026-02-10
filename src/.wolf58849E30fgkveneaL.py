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
    if tag.getText().isdigit() and int(tag.getText()) >= 90 :
        price = tag
        container = price.find_parent("div", class_="item-cell")
        link_tag = container.find("a", class_="item-title")
        link = link_tag.get("href")
        name = link_tag.get_text()
        mappings[link] = price
        print(name)

for k,v in mappings.items():
    print(f'{k} : {v}')