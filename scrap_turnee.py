from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

jucatori = []
f = open("turnee.txt", "r")
url_uri = f.readlines()
url_uri.pop(0)  # primul element din lista e \n
f.close()
f = open("meciuri.txt", "w")
f.close()
f = open("meciuri.txt", "a")
i = 0
for url in url_uri:
    req = Request("https://www.atptour.com" + url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    sursa = soup(webpage, "html.parser")
    meciuri = sursa.find_all("tr")
    for e in meciuri:
        jocuri = e.find_all("td", class_="day-table-name")
        if jocuri:
            for joc in jocuri:
                juc = joc.find_all("a")
                if juc:
                    jucator = juc[0]['href']
                    jucatori.append(str(jucator))
                else:
                    jucatori.append("Bye")
    jucatori.append('\n')
    print(i)
    i+=1
n=i
for jucator in jucatori:
    f.write('\n' + jucator)
f.close()
