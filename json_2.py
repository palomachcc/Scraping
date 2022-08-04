#we simply have key-value pairs.
import json

data="""
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}"""

info = json.loads(data)   #esto convierte data (que estaria sacando de la web) en un objeto estructurado.
print('Len de info:', len(info))
print(info) # Es un diccionario con diccionarios adentro.

print("Name:",info["name"])
print("Hide:",info["email"]["hide"])

exit=input("exit")
