from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

"""
for child in bsObj.find('table', {'id':'giftList'}).children:
    print(child)
"""

for sibling in bsObj.find("table", {'id':'giftList'}).tr.next_siblings:
    print(sibling)

"""
In this code the first title tag is skipped as it cant
be a sibling of itself
"""

print(bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

'''
The .parent gets the parent of the tag and the 
.previouds sibling gets the previous sibling of that
parent tag
'''