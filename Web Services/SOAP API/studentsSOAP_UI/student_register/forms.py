from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_id', 'fullname', 'email',
                  'phoneNumber', 'address', 'entryPoints')
        labels = {
            'fullname': 'Full Name',
            'student_id': 'Admission Number'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['student_id'].required = False
