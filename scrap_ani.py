from selenium import webdriver
from selenium.webdriver.chrome.options import Options

linkuri = []

options = Options()
options.add_argument("--window-size=600,400")
f = open("turnee.txt", "w")
f.close()
for year in range(1915, 2022):
    browser = webdriver.Chrome(options=options)
    url = 'https://www.atptour.com/en/scores/results-archive?year=' + str(year)
    browser.get(url)
    all_links = browser.find_elements_by_class_name('button-border')
    for element in all_links:
        a = element.get_attribute('outerHTML')
        start = False
        link = ""
        for l in a:
            if l == '"' and not start:
                start = True
                continue
            if l == '"' and start:
                break
            if start:
                link += l
        link = "https://www.atptour.com" + link
        linkuri.append(link)
    f = open("turnee.txt", "a")
    for link in linkuri:
        linie = "\n" + link
        f.write(linie)
    f.close()
    browser.quit()
