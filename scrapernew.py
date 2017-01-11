from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup

class Person(object):
    def __init__(self, path):

        soup = BeautifulSoup(urlopen(url + path).read())
        self.name = soup.findAll('h1')[1].string
        self.email = soup.findAll(attrs={"class": "email"})[0].string

    def __str__(self):
        return self.name + "," + self.email


personenliste = []

url = "http://scrapebook22.appspot.com"

html = urlopen(url).read()

soup = BeautifulSoup(html)

csv_file = open("email_list.csv", "w")



for link in soup.findAll("a"):
    if (len(link["href"]) > 3):
        personenliste.append(Person(link["href"]))

for person in  personenliste:
    csv_file.write(person + "\n")


#for person in personenliste:
    #csv_file.write(person)




csv_file.close()