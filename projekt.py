from bs4 import BeautifulSoup #importujemy bibliotekę która umożliwia nam parsowanie stron
from requests import get     #importujemy metodę get, która umożliwia nam pobieranie zawartości 
import sqlite3             #importujemy moduł, który umożliwia nam stworzenie bazy danych i wrzucenie do niej danych
from sys import argv    #importujemy moduł za pomocą którego możemy przekazywać argumenty z lini komend, argv przechowuje nasz argument

def parse_price(price):  # definiujemy funkcje która formatuje nam cenę z OLX'a
    if price=="Zamienię":
        return (price)
    elif price=="Za darmo":
        return (price)
    else:
        return float(price.replace(" ", "").replace("zł", "").replace(",",".")) #zwracamy poprawioną cenę

db=sqlite3.connect("dane.db")  #tworzę połącznie do bazy danych przy użyciu modułu sqlite
cursor=db.cursor()  #tworzę zmienną cursor, która pozwala mi robić operację na bazie danych przy pomocy metody .cursor

#python projekt_1.py setup  <--- za pomocą tej instrukcji w terminalu tworzymy baze danych


if len(argv)>1 and argv[1]=="setup":  #jeśli w terminalu wpiszemy setup (drugi argument) tworzy nam się baza danych 
    cursor.execute("CREATE TABLE offers(name TEXT, price REAL, city TEXT)") #tworzymy baze danych "offers", o kolumnach podanych
    quit()

#page = 1

#liczba_ofert = 0

def parse_page(page):                                            #definiujemy sobie funkcje która parsuje nam stronę
    global liczba_ofert
    print(f"Pracuje nad strona numer {page}")                    #po każdym parsowaniu jednej strony wypisujemy ten komunikat
    URL = f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/malopolskie//?page={page}" 
    #URL = f"https://www.olx.pl/oferty/q-drążek-do-podciągania//?page={page}" 
    #page = page + 1
    strona=get(URL)     #definiujemy zmienną strona która pobiera zawartość strony przy pomocy metody get
    bs=BeautifulSoup(strona.content, 'html.parser') #definiujemy zmienną której zawartością jest nasza strona robimy to za pomocą metody .content
    
    for offer in bs.find_all('div', class_='offer-wrapper'): #za pomocą pętli for przechodzimy po wszystkich ofertach, które zawierają się w divach o klasie podanej
        footer=offer.find('td', class_='bottom-cell')        #definiujemy zmienną footer której zawartość znajduje się w konkretnej ofercie 
        title=offer.find('strong').get_text() #tytuł pobieramy ze znacznika "strong" i pobieramy sam tekst
        location=footer.find('small', class_="breadcrumb x-normal").get_text().strip().split(",")[0] #definiujemy zmienną location, która zawierać będzie lokalizację pobieramy z niej sam tekst i następnie za pomocą .strip usuwamy znaki nowej lini, a następnie rozdzielamy Miasto od dzielnicy (np. Kraków, Podgórze) i zostawiam samo miasto
        try: #używamy instrukcji try except 
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
                
#db=sqlite3.connect("dane.db")
#cursor=db.cursor() 


#print(liczba_ofert)

if len(argv)>1 and argv[1]=="setup":
    cursor.execute("CREATE TABLE offers(name TEXT, price REAL, city TEXT)")
    quit()


for page in range(1,26):
    parse_page(page)


db.close()


