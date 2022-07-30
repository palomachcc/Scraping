
from urllib.request import urlopen
from bs4 import BeautifulSoup

#hay una parte de errores que no aprendi todavia.

count=0
url = input('Enter page:  ') # http://py4e-data.dr-chuck.net/comments_1561778.html
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')           #tags es una lista de : lo que le pida, en este caso el ejercicios me indicaba:You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])   me devuelve el contenido, osea la cantidad de comentarios, para este caso que pedi --soup("span")--.
    #print('Attrs:', tag.attrs)
    count=count + int(tag.contents[0])
    
#print(tags) fijate que si imprimis eso, es una lista. https://www.w3schools.com/python/python_lists.asp    
    
print(count)
exit=input("Press enter to exit")
