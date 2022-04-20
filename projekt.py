from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv 

def parse_price(price):
    if price=="Zamienię":
        return (price)
    elif price=="Za darmo":
        return (price)
    else:
        return float(price.replace(" ", "").replace("zł", "").replace(",","."))

db=sqlite3.connect("dane.db")
cursor=db.cursor() 

#python projekt.py setup


if len(argv)>1 and argv[1]=="setup":
    cursor.execute("CREATE TABLE offers(name TEXT, price REAL, city TEXT)")
    quit()

#page = 1

#liczba_ofert = 0

def parse_page(page):
    global liczba_ofert
    print(f"Pracuje nad strona numer {page}")
    URL = f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/malopolskie//?page={page}" 
    #URL = f"https://www.olx.pl/oferty/q-drążek-do-podciągania//?page={page}" 
    page = page + 1
    strona=get(URL)
    bs=BeautifulSoup(strona.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer=offer.find('td', class_='bottom-cell')
    
        title=offer.find('strong').get_text()
       
        location=footer.find('small', class_="breadcrumb x-normal").get_text().strip().split(",")[0]
        try:
            price=parse_price(offer.find("p", class_="price").get_text().strip())
        except:
            print("brak ceny")
        
        cursor.execute("INSERT INTO offers VALUES (?,?,?)", (title,price,location))
        db.commit()
            #print(location,title,price)
        #liczba_ofert+=1
        if location=="Kraków" and price<150000.0:
            #liczba_ofert+=1
            print(location,title,price)
       
#print(liczba_ofert)
                
db=sqlite3.connect("dane.db")
cursor=db.cursor() 


#print(liczba_ofert)

if len(argv)>1 and argv[1]=="setup":
    cursor.execute("CREATE TABLE offers(name TEXT, price REAL, city TEXT)")
    quit()


for page in range(1,26):
    parse_page(page)


db.close()
