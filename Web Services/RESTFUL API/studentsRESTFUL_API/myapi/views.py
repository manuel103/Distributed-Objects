from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('fullname')
    serializer_class = StudentSerializer
