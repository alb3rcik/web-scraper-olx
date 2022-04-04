from bs4 import BeautifulSoup
from requests import get

page = 1
liczba_ofert = 1
while page != 25:
    URL = f"https://www.olx.pl/oferty/q-drążek-do-podciągania/?page={page}"
    #print(URL)
    #page=get(URL)
    #bs=BeautifulSoup(strona.content, 'html.parser')
    page = page + 1
    strona=get(URL)
    bs=BeautifulSoup(strona.content, 'html.parser')
    #liczba_ofert = 0
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer=offer.find('td', class_='bottom-cell')
        #print(footer)
        title=offer.find('strong').get_text()
        location=footer.find('small', class_="breadcrumb x-normal").get_text().strip().split(",")[0]
        price=offer.find("p", class_="price").get_text().strip()
        #print(location)
        if location =="Kraków":
            print(location,title,price)
            liczba_ofert +=1
print(liczba_ofert)
    

    #sprawdzam czy działa git na surface
    #print(title)
    #print(price)

#URL="https://www.olx.pl/oferty/q-drążek-do-podciągania/"
#page=get(URL)
#bs=BeautifulSoup(page.content, 'html.parser')

#for offer in bs.find_all('div', class_='offer-wrapper'):
 #   footer=offer.find('td', class_='bottom-cell')
    #print(footer)
  #  title=offer.find('strong').get_text()
   # location=footer.find('small', class_="breadcrumb x-normal").get_text().strip().split(",")[0]
    #price=offer.find("p", class_="price").get_text().strip()
    #print(location)
    #if location =="Kraków":
     #   print(location,title,price)

    #sprawdzam czy działa git na surface
    #print(title)
    #print(price)