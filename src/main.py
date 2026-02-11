import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/s?k=graphics+cards&crid=1IV82F8UL4HFB&qid=1770823482&sprefix=graphics+cards%2Caps%2C99&xpid=-BpzREDtw_auY&ref=sr_pg_1"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("span", class_="a-price-whole")

def get_link(tag):
    pass

def get_info_from_tag(tag, target=None):

    container = tag.find_parent("div", attrs={"data-component-type": "s-search-result"})
    if not container:
        return None
    
    h2 = container.find("h2")
    if h2:
        name = h2.get("aria-label")
    else:
        return None
    
    if target.lower() not in name:
        return None

    price = container.find("span", class_="a-offscreen").get_text()
    if not price:
        return None

    link_tag = container.find("a", class_="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal")
    link = "https://www.amazon.co.uk" + link_tag.get("href")

    return {
        "price": price,
        "link": link,
        "name": name,
    }
    

def main():
    while True:
        name = input("GPU to search for: ")
        items = []
        for tag in tags:
            if item := get_info_from_tag(tag, name):
                items.append(item)
        if not items:
            print("None found")
        else:
            break
        
    mode = input("Mode: ")
    sort_field = "price"
    if mode == "min":
        selected_item = min(items, key=lambda i: i[sort_field])
    elif mode == "max":
        selected_item = max(items, key=lambda i: i[sort_field])
    else:
        raise ValueError("mode must be 'min' or 'max'")
    
    link = selected_item["link"]
    count = len(link)
    text = "link to gpu"

    #hyperlink
    hyperlink = f'\033]8;;{link}\033\\{text}\033]8;;\033\\'

    print(f"Found {count}")
    print(hyperlink)

main()