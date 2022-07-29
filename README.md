# Scraping
Scraping Numbers from HTML using urllib

Using urllib, you can treat a web page much like a file. You simply indicate which web page you would like to retrieve and urllib handles all of the HTTP protocol and header details. Once the web page has been opened with urllib.urlopen, we can treat it like a file and read through it using a for loop.
Antes de poder utilizar las funciones de un módulo, debemos importarlo a nuestro programa. Para hacer eso, utilizaremos la declaración import seguida del nombre del o los módulos que se desen importar. Por ej:

    import urllib.request    #importo la libreria. Esta tiene 4 modulos, el que uso aca es el .request
    
Luego podemos utilizar las funciones incluídas en ambos módulos escribiendo el nombre del mismo seguido por un punto y la función deseada.

----Modulo Request----

urllib.request.urlopen (url, data=None, otras cosas)
Open the URL url, which can be either a string or a Request object. url should be a string containing a valid URL. Por ejemplo:
    
    page=input("Enter de page: ")
    fhand = urllib.request.urlopen(page)       # urlopen() es la funcion del modulo request
