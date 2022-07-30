from urllib.request import urlopen
from bs4 import BeautifulSoup

url="http://py4e-data.dr-chuck.net/known_by_Hafswa.html"
html= urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

#print(html) # me devuelve bytes
#print(soup.prettify()) me devuelve el codigo html ordenado

#for link in soup.find_all('a'):  # le pido que me devuelva de "la sopa" todos los links
#    print(link.get('href'))

#tags=soup("a") # equivale a lo mismo que decir: links=soup.find_all("a")
#print(tags) #esto me devuelve una lista con varias cosas, no solamente el href como arriba

tags=soup.find_all("a")
print(tags)

exit=input("press enter to exit")
