from selenium import webdriver
from selenium.webdriver.chrome.options import Options

linkuri = []
f = open("turnee.txt", "r")
options = Options()
options.add_argument("--window-size=600,400")
url_uri = f.readlines()
url_uri.pop(0)  # primul element din lista e \n

browser = webdriver.Chrome(options=options)
browser.get(url_uri[2])
rezultate = browser.find_elements_by_tag_name('tr')
for meci in rezultate:
    a = meci.get_attribute('outerHTML')
    print(a)
browser.quit()
