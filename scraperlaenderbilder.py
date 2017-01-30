from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup
import requests


class Land(object):
    def __init__(self, country, capital):
        self.country=country
        self.capital=capital
    def __str__(self):
        return self.country + "," + self.capital




def laender():
    url = "https://www.countries-ofthe-world.com/capitals-of-the-world.html"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)

    csv_file = open("laender_list.csv", "w")

    laenderliste = []


    table = soup.findAll("td", attrs={"class":None})
    for count, i in enumerate(table):
        if count % 2 == 0:
            country = i.getText()
        else:
            capital = i.getText()

            country = country.encode("utf-8")
            capital = capital.encode("utf-8")

            stadteliste.append(capital)


    return country, capital


url = "https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order"
r = requests.get(url)
data = r.text
bildersoup = BeautifulSoup(data)
stadteliste = []
linkliste = []
for stadt in stadteliste:
    print stadt



print linkliste
















