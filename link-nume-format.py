f = open("meciuri.txt", "r")
url_uri = f.readlines()
url_uri.pop(0)
f.close()
i = 0
f = open("meciuri.csv", 'w')
while i < 419892:
    if len(url_uri[i].split("/")) > 3 and len(url_uri[i + 1].split("/")) > 3:
        meci = url_uri[i].split("/")[3] + "," + url_uri[i + 1].split("/")[3] + '\n'
        f.write(meci)
    i += 2
f.close()
