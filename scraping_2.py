
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


count=0
url = input('Enter page:  ') # http://py4e-data.dr-chuck.net/comments_1561778.html
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    count=count + int(tag.contents[0])

print(count)
exit=input("Press enter to exit")
