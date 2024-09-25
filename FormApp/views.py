from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentModelForm, StudentUpdateForm
from .models import Student
from django.contrib import  messages
from django.conf import settings


def home(request):
    return render(request,'FormApp/home.html')
def create_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Student Created Successfully")
                form = StudentModelForm()
            except:
                pass
        else:
            print("Form errors:", form.errors)
            messages.error(request,"Please try another")
    else:
        form = StudentModelForm()

    return render(request, 'FormApp/create_student.html', {'form': form})


def showAllStudents(request):
    students = Student.objects.all()
    return render(request, 'FormApp/showAllStudents.html', {'students': students})

def updateStudent(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("showAllStudents")
        else:
            print("Form errors:", form.errors)  # Print the errors here
    else:
        form  = StudentModelForm(instance=student)  # Pass the instance for initial values

    context = {
        "form":form,
        "student":student
    }
    return render(request, 'FormApp/updateStudent.html',context)

def deleteStudent(request,student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request,"Student Deleted")
    return redirect("showAllStudents")

def send_email(request):
    if request.method =='POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                messages.success(request,'Email sent successfully')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request,'All fields are required')

    return render(request,'FormApp/send_email.html')