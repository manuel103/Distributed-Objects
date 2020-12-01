from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. for insert operation
    path('', views.student_form, name='student_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.student_form, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    # get req. to retrieve and display all records
    path('list/', views.student_list, name='student_list'),

]
