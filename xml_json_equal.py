import xml.etree.ElementTree as ET

data_xml = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''


#----------------------------------------------------------
#Here is a JSON encoding that is roughly equivalent to the simple XML from above:

data_json="""
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


print("XML:\n",data_xml,"\n")
print("JSON:\n",data_json,"\n")

exit=input("press enter to exit")
