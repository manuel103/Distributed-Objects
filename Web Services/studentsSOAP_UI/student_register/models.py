from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=30)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    entryPoints = models.CharField(max_length=15)
