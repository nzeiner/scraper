from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup

class Person(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
    def __str__(self):
        return self.name + "(" + self.email + ")"


personenliste = []


url = "http://scrapebook22.appspot.com"

html = urlopen(url).read()

soup = BeautifulSoup(html)

csv_file = open("email_list.csv", "w")


def getEmail(path):
    html = urlopen(url + path).read()
    soup = BeautifulSoup(html)
    email = soup.findAll(attrs={"class":"email"})[0].string
    csv_file.write(email + "\n")
    return email

def getName(path):
    html = urlopen(url + path).read()
    soup = BeautifulSoup(html)
    name = soup.findAll("h1")[1].string
    csv_file.write(name + "\n")
    return name


for link in soup.findAll("a"):
    if (len(link["href"]) > 3):
        email = getEmail(link["href"])
        name= getName(link["href"])

        personenliste.append(Person(name,email))



        #print getEmail(link["href"]) #um auf Attribute zuzugreifen wird der link wie ein Dictionary behandelt (eckige Klammer)


for person in personenliste:
    print person

csv_file.close()
