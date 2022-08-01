#Extracting Data from XML
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_42.xml

# NOTE: To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
#       counts = tree.findall('.//count')

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


# para que usa urllib? para LEER LA URL

url=input("Enter url:")
data= urllib.request.urlopen(url).read()
com_sum=0
#print(data)  # me devuelve bytes
#print(data.decode()) #me devuelve el codigo lindo


#----------------------------------------------------Opcion A
#tree=ET.fromstring(data)
#lst=tree.findall("comments/comment")
#print(lst) me devuelve una lista de tags
#for item in lst:
#    #print("N° of comments:",item.find("count").text)
#    int_com_count=int(item.find("count").text)
#    com_sum=com_sum+int_com_count

#-----------------------------------------------------Oocion B
tree=ET.fromstring(data)
lst = tree.findall('.//count')
#print(lst)
for item in lst:
    #print("N° of comments:",item.text)
    int_com_count=int(item.text)
    com_sum=com_sum+int_com_count







print(com_sum)
exit=input("press enter to exit")
