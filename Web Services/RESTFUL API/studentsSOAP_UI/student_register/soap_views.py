from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from .models import Student


class SoapService(ServiceBase):
    @rpc(Integer(nillable=False), _returns=Unicode)
    def student_details(ctx, student_id):
        return_value = "Student doesn't exist."
        try:
            student_info = Student.objects.get(student_id=student_id)
            return_value = 'Name: {}\nEmail: {}\nPhone Number: {}\nAddress: {}\nEntry points: {}'.format(
                student_info.fullname, student_info.email, student_info.phoneNumber, student_info.address, student_info.entryPoints)
        except:
            print("Details Not Available")
        return return_value


soap_app = Application(
    [SoapService],
    tns='django.studentsSOAP_UI.student_register',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
student_soap = csrf_exempt(django_soap_application)
