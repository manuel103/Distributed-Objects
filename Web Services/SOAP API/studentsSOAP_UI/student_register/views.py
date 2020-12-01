from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = StudentForm.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')


def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')

# def client(request):
#     context = {'student_details': Student.objects.all()}
#     return render(request, "student_register/student_client.html", context)


def client(request):
    query = request.GET.get('search_res', None)
    context = {}

    if query and request.method == 'GET':
        results = Student.objects.filter(student_id=query)
        context.update({'results': results})

    return render(request, 'student_register/student_client.html', context)

