from bs4 import BeautifulSoup
from requests import get

URL="https://www.olx.pl/oferty/q-drążek-do-podciągania/"
page=get(URL)
bs=BeautifulSoup(page.content, 'html.parser')
for offer in bs.find_all('div', class_='offer-wrapper'):
    footer=offer.find('td', class_='bottom-cell')
    #print(footer)
    title=offer.find('strong').get_text()
    location=footer.find('small', class_="breadcrumb x-normal").get_text().strip().split(",")[0]
    price=offer.find("p", class_="price").get_text().strip()
    #print(location)
    if location =="Kraków":
        print(location,title,price)

    #sprawdzam czy działa git
    #print(title)
    #print(price)