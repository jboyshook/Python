import xml.etree.ElementTree as ET

INPUT_1 = '''
<stuff>   
  <users>
    <user x = "2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x = "7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(INPUT_1)
lst = stuff.findall("users/user")
print("User count:", len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribuite', item.get('x'))


"""
The findall method retrives a list of all subtree 
that represent user structures in the xml tree. Then 
we write a loop to look at the user nodes and print 
the name and id
"""

"""
Enter the parent directory of the node till it reaches
the root node excluding the root node
"""
