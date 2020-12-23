import requests
from bs4 import BeautifulSoup

URL = 'https://www.bestbuy.com/site/microsoft-controller-for-xbox-series-x-xbox-series-s-and-xbox-one-latest-model-shock-blue/6430660.p?skuId=6430660'

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("div", class_="sku-title").get_text()
price = soup.find(
    "div", class_="priceView-hero-price priceView-customer-price").get_text(strip=True)


converted_price = price[0:100]


print(title)
print(converted_price)
print(URL)

URLN = 'https://www.newegg.com/p/pl?d=rtx&N=100007709%20601357282&isdeptsrh'
pagen = requests.get(URLN, headers=headers)
soupn = BeautifulSoup(pagen.content, "html.parser")

cards = soupn.find_all('div', {'class':'item-cell'})

for card in cards:
    card_title = card.find('a',{'class':'item-title'})
    card_price = card.find('li', {'class':'price-current'})
    try:
        if (card_price.text != ""):
            print(card_title.text)
            print(" ")
            print(card_price.text)
            print(" ")
            print(card_title['href'])

    except:
        pass
    
    # print(card_price)
# print(cards)
