from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bsObj = BeautifulSoup(html, "html.parser")

#Prints the h1 tags
#print(bsObj.h1)
print(bsObj.prettify())

#We can also run into connection errors so we
#use a try except block
#check in bs1.py
