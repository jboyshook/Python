#PARSING XML IN PYTHON

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type = "intl">
    +1 734 303 4456
  </phone>
  <email hide = "yes" />
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))

"""
Calling the formatstring funcion converts the xml into a 
tree the find function seraches through the tree and retrieves 
the element
"""
