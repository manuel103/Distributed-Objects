'''' serializing XML file to JSON '''

import json
import xmltodict
import pprint

with open("serialization/students.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    json_data = json.dumps(data_dict)

    # write json data to output
    with open("serialization/students.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()

    pretty = pprint.PrettyPrinter(indent=4)
    pretty.pprint(json_data)
    