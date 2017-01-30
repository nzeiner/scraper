from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
import requests


class Land(object):
    def __init__(self, country, capital):
        self.country=country
        self.capital=capital
    def __str__(self):
        return self.country + "," + self.capital

    def _dict_(self):
        return str(country) + str(capital)


url = "https://www.countries-ofthe-world.com/capitals-of-the-world.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

csv_file = open("laender_list.csv", "w")

laenderliste = []
laenderdic = {}

table = soup.findAll("td", attrs={"class":None})
for count, i in enumerate(table):
    if count % 2 == 0:
        country = i.getText()
    else:
        capital = i.getText()

        country = country.encode("utf-8")
        capital = capital.encode("utf-8")

        laenderdic[Land(country,capital)] = Land(country, capital)
        laenderliste.append(Land(country,capital))


for ding in laenderliste:
    csv_file.write(str(ding) + "\n")

print laenderdic

print laenderliste












