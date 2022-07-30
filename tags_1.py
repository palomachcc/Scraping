from bs4 import BeautifulSoup

# NOTE: La comilla triple nos permite insertar un string con todas las líneas que deseemos. Basta que enmarquemos un bloque de texto entre comillas triples (da igual si son simples o dobles) y Python respetará el aspecto y formato completo del texto. Todo eso en un único string.

html ="""<div>something</div>
<div>something else</div>
<div class='magical'>hi there</div>
<p>ok</p>"""

soup = BeautifulSoup(html, "html.parser")

print([tag.name for tag in soup.find_all()])
# ['div', 'div', 'div', 'p']

print([str(tag) for tag in soup.find_all()])
# ['<div>something</div>', '<div>something else</div>', '<div class="magical">hi there</div>', '<p>ok</p>']

exit=input("\nPress enter to exit")
