from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

url = input('Enter page:  ') # http://py4e-data.dr-chuck.net/known_by_Hafswa.html
tag_count=0
rep_number=input("Enter count:")
rep_number=int(rep_number)
rep_count=0
tag_number=input("Enter position:")
tag_number=int(tag_number)


while rep_count<rep_number:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the anchor tags
    tags = soup('a')
    tag_count=0
    for tag in tags:
    # Look at the parts of a tag
        tag_count=tag_count + 1
        if tag_count==tag_number:
            print('URL n°',tag_count,":", tag.get('href', None))
            break
    url=tag.get('href', None)
    rep_count=rep_count+1




exit=input("Press enter to exit")
