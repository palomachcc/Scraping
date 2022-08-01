import xml.etree.ElementTree  as ET   #el as me permite renombrarlo asi no escxri

data="""<person>
<name>Chuck</name>
<phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>"""

#armas el arbol de xml y buscas por ahi...
tree=ET.fromstring(data)
#uso la libreria que llame ET, para que agarre todo ese parrafo y me devuelva un arbol
#Calling fromstring converts the string representation of the XML into a “tree” of XML elements. When the XML is in a tree, we have a series of methods we can call to extract portions of data from the XML string. The find function searches through the XML tree and retrieves the element that matches the specified tag.
print("name:",tree.find("name").text) # le digo que me encuentre el tag "name" el.text le dice qwue me devuelva el nombre entre esoss tags
print("attr:",tree.find("email").get("hide")) # le pedis que te devuelva una partecita del arbol donde esta el email y que de ahi te de el atribudo hide


exit=input("press enter to exit")
