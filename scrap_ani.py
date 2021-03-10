from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

f = open("turnee.txt", "w")
f.close()


for year in range(1920, 2022):
    url = 'https://www.atptour.com/en/scores/results-archive?year=' + str(year)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    sursa = soup(webpage, "html.parser")
    turnee = sursa.find_all("a", class_="button-border")
    f = open("turnee.txt", "a")
    for turneu in turnee:
        f.write('\n' + str(turneu['href']))
    f.close()
