#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON
# data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the
# sum
import urllib.request
import json


count=0
link=input("Enter URL:")
url = urllib.request.urlopen(link)
data = url.read().decode()

#print (data)   #Hasta aca, lo que hace es abrir y leer el contenido de la pagina. data es un diccionario
#print("len data",len(data)) # 2711

data_estructurada = json.loads(data)

#print(json.dumps(data_estructurada, indent=4))   #sin esto me imprime todo en un parrafo
#print('len data_estructurada:', len(data_estructurada)) #2   estan "note" y "comments"


for item in data_estructurada["comments"]:
    #print("comentarios:", item["count"])
    count=count+item["count"]

print(count)


exit=input("exit")
