from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:8000/soap_api/?WSDL', cache=NoCache())
print (my_client)
print ('Student details:\n', my_client.service.student_details(15))
