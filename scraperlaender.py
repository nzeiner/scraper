from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup

class Person(object):
    def __init__(self, path):

        soup = BeautifulSoup(urlopen(url + path).read())
        self.name = soup.findAll('h1')[1].string
        self.email = soup.findAll(attrs={"class": "email"})[0].string

    def __str__(self): #definiert was passiert wenn aus daten ein string gemacht wird - bei print passiert das von vornherein
        return self.name + "," + self.email







laenderliste = []

laenderdic = {}

url = "https://www.countries-ofthe-world.com/capitals-of-the-world.html"

html = urlopen(url).read()

soup = BeautifulSoup(html)

csv_file = open("email_list.csv", "w")



for link in soup.findAll("a"):
    if (len(link["href"]) > 3):
        personenliste.append(Person(link["href"]))






for person in  personenliste:
    csv_file.write(str(person) + "\n")


#for person in personenliste:
    #csv_file.write(person)




csv_file.close()