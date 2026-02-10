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
    price = tag.get_text().replace(",", "")
    if price.isdigit() and int(price) >= 90:
        container = tag.find_parent("div", class_="item-cell")
        link_tag = container.find("a", class_="item-title")
        link = link_tag.get("href")
        name = link_tag.get_text()
        price = int(price.strip())
        mappings[price] = [link, name]


cheapest_price = max(mappings.keys())
cheapest_link = mappings[cheapest_price][0]
cheapest_name = mappings[cheapest_price][1]
print(cheapest_link)
