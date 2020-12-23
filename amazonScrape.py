import requests
from bs4 import BeautifulSoup

URL = 'https://www.bestbuy.com/site/microsoft-controller-for-xbox-series-x-xbox-series-s-and-xbox-one-latest-model-shock-blue/6430660.p?skuId=6430660'

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("div", class_="sku-title").get_text(strip=True)
price = soup.find(
    "div", class_="priceView-hero-price priceView-customer-price").get_text(strip=True)


converted_price = price[0:100]


print(title)
print(converted_price)
print(URL)

URLN = 'https://www.newegg.com/p/pl?d=rtx+3080&N=100007709%208000%20601357282&isdeptsrh=1'
pagen = requests.get(URLN, headers=headers)
soupn = BeautifulSoup(pagen.content, "html.parser")

cards = soup.find_all()

for c in cards:
    print(c.get_text(strip=True))
