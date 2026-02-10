import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("strong")

def get_info_from_tag(tag):
    """Extract a GPU listing from a price tag element if it looks valid.

    This parses the tag's text as a price, filters out low or invalid prices,
    and returns metadata about the associated product listing.

    Args:
        tag: A BeautifulSoup tag that is expected to contain a price.

    Returns:
        dict | None: A dictionary with "price", "link", and "name" keys if the
        tag represents a valid item, otherwise None.
    """
    
    price_text = tag.get_text().replace(",", "")
    if not price_text.isdigit():
        return None

    price = int(price_text)
    if price < 90:
        return None

    container = tag.find_parent("div", class_="item-cell")
    if not container:
        return None

    if link_tag := container.find("a", class_="item-title"):
        return {
            "price": price,
            "link": link_tag.get("href"),
            "name": link_tag.get_text(strip=True),
        }
    else:
        return None


def main():
    items = []
    for tag in tags:
        if item := get_info_from_tag(tag):
            items.append(item)
            
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



