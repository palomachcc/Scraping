from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors. SIN ESTO NO CORRE A VECES
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=0
url = input('Enter page:  ') # http://py4e-data.dr-chuck.net/comments_1561778.html
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# #proba con http://py4e-data.dr-chuck.net/known_by_Hafswa.html para ver links y con http://py4e-data.dr-chuck.net/comments_1561778.html para ver comentarios
tags = soup('span')           #tags es una lista de : lo que le pida, en este caso el ejercicios me indicaba:You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])   me devuelve el contenido, osea la cantidad de comentarios, para este caso que pedi --soup("span")--.
    #print('Attrs:', tag.attrs)
    count=count + int(tag.contents[0])
    
#print(tags) fijate que si imprimis eso, es una lista. https://www.w3schools.com/python/python_lists.asp    me devuelve todo lo que tiene "span"
#print([tag.name for tag in soup.find_all()]) me da una lista de todos los tags que aparecen en la pagina
 
print(count)
exit=input("Press enter to exit")


