#we simply have key-value pairs.
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)        #usa la funcion loads() de la libreria json para obtener una lista. Cada item de la lista es a su vez un diccionario (respectivo a cada usuario)
#the returned data is simply native Python structures. asi que luego manejo la info con la sintaxis de python

print('User count:', len(info),"\n")        #each user is a set of key-value pairs.
 # me devuelve que tengo dos elementos. cada uno corresponde a un usuario

print("lo que me devuelve json.loads(data)\n",info,"\n")            # info es una lista [] de dos diccionarios {}


for item in info:                    #item es un diccionario
    print('Name', item['name'])      # para imprimir items de diccionarios, en python, pongo diccionario["nombre de lo que quiero"] ---> item["name"] dame el name dentro de cada item
    print('Id', item['id'])
    print('Attribute', item['x'])

exit=input("exit")
