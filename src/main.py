import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

strong_tags = soup.find_all("strong")

