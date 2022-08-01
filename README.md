# Scraping ----> Que es y para que sirve---> https://www.youtube.com/watch?v=2XiLA_dEteQ

La idea es recorrer el codigo HTML para sacar info de ahi. 

Scraping Numbers from HTML using urllib and BeautifulSoup

----Modulo Request de urllib----

Using urllib, you can treat a web page much like a file. You simply indicate which web page you would like to retrieve and urllib handles all of the HTTP protocol and header details. Once the web page has been opened with urllib.urlopen, we can treat it like a file and read through it using a for loop.
Antes de poder utilizar las funciones de un módulo, debemos importarlo a nuestro programa. Para hacer eso, utilizaremos la declaración import seguida del nombre del o los módulos que se desen importar. Por ej:

    import urllib.request    #importo la libreria. Esta tiene 4 modulos, el que uso aca es el .request
    
Luego podemos utilizar las funciones incluídas en ambos módulos escribiendo el nombre del mismo seguido por un punto y la función deseada.

FUNCION: urllib.request.urlopen (url, data=None, otras cosas)
Open the URL url, which can be either a string or a Request object. url should be a string containing a valid URL. Por ejemplo:
    
    page=input("Enter de page: ")
    fhand = urllib.request.urlopen(page)       # urlopen() es la funcion del modulo request

----BeautifulSoup de bs4----

NOTA: hay varias formas de importar modulos de una libreria --->https://blog.cloudboost.io/python-import-from-as-cheatsheet-tutorial-example-beginner-help-module-function-def-5f03b02a1dbe

    from bs4 import BeautifulSoup

TAGS https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup , https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
A Tag object corresponds to an XML or HTML tag in the original document: https://www.w3schools.com/TAgs/default.asp 

One common task is extracting all the URLs found within a page’s <a> tags:

    for link in soup.find_all('a'):
        print(link.get('href'))
        
Another common task is extracting all the text from a page:

    print(soup.get_text())
    


DATA SERIALIZATION 

Data serialization is the process of converting an object into a stream of bytes to more easily save or transmit it. Byte streams are a sequence of bytes used by programs to input and output information.Data serialization is the process of converting data objects present in complex data structures into a byte stream for storage, transfer and distribution purposes on physical devices.

Computer systems may vary in their hardware architecture, OS, addressing mechanisms. Internal binary representations of data also vary accordingly in every environment. Storing and exchanging data between such varying environments requires a platform-and-language-neutral data format that all systems understand.

-----parse XML (eXtensible Markup Language) data-----

https://www.py4e.com/html3/13-web
https://docs.python.org/3/library/xml.etree.elementtree.html
    Basicamente, es arboles, listas de arboles e indagar por las ramas de los arboles
Using an XML parser such as ElementTree has the advantage that while the XML in this example is quite simple, it turns out there are many rules regarding valid XML, and using ElementTree allows us to extract data from XML without worrying about the rules of XML syntax.
Calling fromstring converts the string representation of the XML into a “tree” of XML elements. When the XML is in a tree, we have a series of methods we can call to extract portions of data from the XML string. The find function searches through the XML tree and retrieves the element that matches the specified tag.
    
    
    
IMPORTACION de librerias

La forma en que llamas a una funcion depende de como importaste. Si no esta bien, no corre el codigo.

from urllib.request import urlopen ---> html = urlopen(url, context=ctx).read() (aca no usa decode porque despues usa el parser de BS)
import urllib.request ---> html= urllib.request.urlopen(page).read().decode()



----Parsing JavaScript Object Notation (JSON)----


