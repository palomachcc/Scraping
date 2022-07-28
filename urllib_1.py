import urllib.request    #importo la libreria. Esta tiene 4 modulos, el que uso aca es el .request


page=input("Enter de page: ")
fhand = urllib.request.urlopen(page) # http://www.dr-chuck.com/page1.htm o http://data.pr4e.org/romeo.txt

for line in fhand:
    print(line.decode().strip())

exit=input("\nPulse enter para salir")
