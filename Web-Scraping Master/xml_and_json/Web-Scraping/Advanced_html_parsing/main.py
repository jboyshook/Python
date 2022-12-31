from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())


"""
The bsObj.findAll() takes two vars (tagName, tagAttribuites)
In this case the span tag and class with green which makes the color green
"""