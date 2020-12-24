import os
import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203090%5Esoldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items'

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

print("Bestbuy:\n\n")
items = soup.find_all('div', {'class':'sku-item'})
for item in items:
    title = soup.find("h4", class_="sku-header").get_text()
    price = soup.find("div", class_="priceView-hero-price priceView-customer-price").get_text()
    print(title,"\n")
    print(price,"\n")

print("Newegg:\n\n")
URLN = 'https://www.newegg.com/p/pl?d=rtx&N=100007709%20601357282'
pagen = requests.get(URLN, headers=headers)
soupn = BeautifulSoup(pagen.content, "html.parser")

cards = soupn.find_all('div', {'class':'item-cell'})

for card in cards:
    card_title = card.find('a',{'class':'item-title'})
    card_price = card.find('li', {'class':'price-current'})
    try:
        if (card_price.text != ""):
            print(card_title.text,"\n")
            print(card_price.text,"\n")
            print(card_title['href'],"\n")

    except:
        pass

print("Reddit:\n\n")
    
URLR = 'https://www.reddit.com/r/buildapcsales/new/'
pager = requests.get(URLR, headers=headers)
soupr = BeautifulSoup(pager.content, "html.parser")

posts = soupr.find_all('div', {'class':'Post'})

for post in posts:
    post_title = post.find('h3')
    expired_post = post.find(href=re.compile("Expired"))
    print(post_title.text)


