from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentModelForm, StudentUpdateForm
from .models import Student
from django.contrib import  messages

def create_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Student Created Successfully")
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
    print(student)
    student.delete()
    messages.success(request,"Student Deleted")
    return redirect("showAllStudents")