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

info = json.loads(data)                                        #usa la funcion loads() de la libreria json
print('User count:', len(info),"\n")                               # me devuelve que tengo dos elementos. cada uno corresponde a un usuario
print("lo que me devuelve json.loads(data)\n",info,"\n")            # info es una lista [] de dos diccionarios {}


for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

exit=input("exit")
