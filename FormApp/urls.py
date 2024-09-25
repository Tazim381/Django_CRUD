from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_student', views.create_student, name="create_student"),
    path('showAllStudents',views.showAllStudents, name='showAllStudents'),
    path('updateStudent/<int:student_id>/', views.updateStudent, name='updateStudent'),
    path('deleteStudent/<int:student_id>/', views.deleteStudent,name = 'deleteStudent'),
    path('send_email', views.send_email, name='send_email'),

]
