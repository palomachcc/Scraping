import xml.etree.ElementTree as ET

data= """
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>"""

stuff = ET.fromstring(data) #Calling fromstring converts the string representation of the XML into a “tree” of XML elements.
lst = stuff.findall("users/user") #Element.findall() finds only elements with a tag which are direct children of the current element. users/user quiere decir dentro de la parte de "users" dame los "user"
print("User count:", len(lst))
print("print(lst):\n",lst)
#for item in lst:   #lst es una lista de arbolitos. y puedo buscar en la lista, en cada arbol y en las "ramas" de los arbolitos
#    print('Name', item.find('name').text) #Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content.
#    print('Id', item.find('id').text)
#    print('Attribute', item.get('x')) #Element.get() accesses the element’s attributes

exit=input("press enter to exit")
