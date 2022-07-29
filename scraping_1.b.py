#Tengo una URL: http://py4e-data.dr-chuck.net/comments_1561778.html ,contiene una tabla de nombres y recuentos de comentarios.

import urllib.request    #importo la libreria. Esta tiene 4 modulos, el que uso aca es el .request
from bs4 import BeautifulSoup


page=input("Enter de page: ")
html= urllib.request.urlopen(page).read().decode()
print(html)


exit=input("\nPulse enter para salir")
