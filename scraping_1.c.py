import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("enter URL: ") # http://www.dr-chuck.com/page1.htm
html=urllib.request.urlopen(url).read()   #html me devuelve un UTF-8 string
soup=BeautifulSoup(html,"html.parser")    #con BS hace "limpieza", le entregas la cosa "html" y nos devuelve un objeto limpio

print(soup)



exit=input("Presione enter para salir")
