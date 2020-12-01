'''' deserializing JSON file to XML '''

from json2xml import json2xml
from json2xml.utils import readfromjson


data = readfromjson("deserialization/students.json")
xml_data = json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml()
print(xml_data)

# write xml data to output
with open("deserialization/students.xml", "w") as xml_file:
    xml_file.write(xml_data)
    xml_file.close()
