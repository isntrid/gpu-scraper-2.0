import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

main = soup.find_all("strong")
decimal = soup.find_all("sup")
import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

price_whole_elements = soup.find_all("strong")
price_fraction_elements = soup.find_all("sup")

for whole_elem, fraction_elem in zip(price_whole_elements, price_fraction_elements):
    whole_text = whole_elem.get_text(strip=True)
    fraction_text = fraction_elem.get_text(strip=True)

    if whole_text.isdigit():
        print(f"{whole_text}{fraction_text}")
