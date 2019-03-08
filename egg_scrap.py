from bs4 import BeautifulSoup
import requests

new_egg_url = "https://www.newegg.com/global/il-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=video+card"
page = requests.get(new_egg_url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
# print(soup.h1)
# print(soup.p)
# print(soup.body.span)

containers = soup.findAll("div", {"class": "item-container"})
print(len(containers))

for container in containers:
    card_info = container.a
    card_text = card_info.img["alt"]
    # print(type(card_text))
    if "Video Card" in card_text:
        # this is full line output example below
        # MSI GeForce RTX 2080 DirectX 12 RTX 2080 VENTUS 8G OC 8GB 256-Bit GDDR6 PCI
        # Express 3.0 x16 HDCP Ready SLI Support Video Card
        print(card_info.img["alt"] + " ----> " + str(containers.index(container)))
        # this is only Brand name
        # print(card_text.split(' ', 1)[0])
        brand = card_text.partition(' ')[0]
        # print(brand)
