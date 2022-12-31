from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:  #type:ignore
    print(e)

else:
    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj.prettify())

"""
This Code Takes cares of errors
"""