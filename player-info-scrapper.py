from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re

jucatori = []
f = open("meciuri.txt", "r")
url_uri = f.readlines()
f.close()
urls = []
for url in url_uri:
    if url != '\n' or 'Bye':
        urls.append(url[:-1])
urls = set(urls)
print(urls)
f = open("player-info.txt", "w")

for url in urls:
    f=open("player-info.txt", "a")
    try:
        req = Request("https://www.atptour.com" + url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        sursa = soup(webpage, "html.parser")
        card = sursa.find(id="playerProfileHero")
        try:
            nume = card.find(class_="last-name").text
        except:
            nume = " "
        try:
            prenume = card.find(class_="first-name").text
        except:
            prenume = " "
        try:
            tara = card.find(class_="player-flag-code").text
        except:
            tara = " "
        try:
            greutate = card.find(class_="table-weight-kg-wrapper").text
            greutate = re.findall(r'\d+', greutate)[0]
        except:
            greutate = " "
        try:
            inaltime = card.find(class_="table-height-cm-wrapper").text
            inaltime = re.findall(r'\d+', inaltime)[0]
        except:
            inaltime = " "
        f.write(nume + " " + prenume + " " + tara + " " + greutate + " " + inaltime + "\n")
        f.close()
        # truri = sursa.find_all("tr")
        # stats = truri[2]
    except:
        print("Fail")
# print(truri[2])
# print(card)
f.close()
