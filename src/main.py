import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("strong")

items = []
for tag in tags:
    price_text = tag.get_text().replace(",", "")
    if price_text.isdigit() and int(price_text) >= 90:
        container = tag.find_parent("div", class_="item-cell")
        link_tag = container.find("a", class_="item-title")
        link = link_tag.get("href")
        name = link_tag.get_text(strip=True)
        price = int(price_text)

        items.append(
            {
                "price": price,
                "link": link,
                "name": name,
            }
        )

mode = input("Mode: ")  
sort_field = "price"


if mode == "min":
    selected_item = min(items, key=lambda i: i[sort_field])
elif mode == "max":
    selected_item = max(items, key=lambda i: i[sort_field])
else:
    raise ValueError("mode must be 'min' or 'max'")

display_field = input("Display: ")

print(selected_item[display_field])
