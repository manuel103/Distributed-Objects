import sqlite3
import json
import collections
from json2xml import json2xml
from json2xml.utils import readfromjson


conn = sqlite3.connect('database/students.db')
cursor = conn.cursor()  # allows sql commands execution

# Create students table
cursor.execute("""CREATE TABLE students (
    name text,
    std_class text,
    year integer
)""")

"""Adding data to table"""
cursor.execute("INSERT INTO students(name, std_class, year) VALUES ('John', '3A', '2019'), ('Flix', '3B', '2019'), ('Leah', '4c', '2020')")
conn.commit()

"""Querying the database to fetch all data"""
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
# print(rows)
conn.commit()
conn.close()

"""Serializing the query output to a JSON object & 
building a list of dictionaries with key-value pairs"""

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['name'] = row[0]
    d['std_class'] = row[1]
    d['year'] = row[2]
    objects_list.append(d)

j = json.dumps(objects_list)

with open('database/student_objects.json', 'w') as f:
    f.write(j)

"""Deserializing the JSON output to print an xml format"""
data = readfromjson("database/student_objects.json")
xml_data = json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml()
print(xml_data)

# saving the xml data to output file
with open("database/student_objects.xml", "w") as xml_file:
    xml_file.write(xml_data)
    xml_file.close()
