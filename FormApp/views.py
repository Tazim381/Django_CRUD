from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentModelForm, StudentUpdateForm,UserForm,UserProfileForm,LoginForm
from .models import Student
from django.contrib import  messages
from django.conf import settings
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout

@login_required
def home(request):
    return render(request,'FormApp/home.html')

@login_required
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

@login_required
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
@login_required
def deleteStudent(request,student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request,"Student Deleted")
    return redirect("showAllStudents")
@login_required
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


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form= UserForm()
        profile_form = UserProfileForm()
    return render(request,'FormApp/register.html',{'user_form':user_form, 'profile_form':profile_form})

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username)

            user = authenticate(request,username= username, password= password)
            print(user)
            if user:
                auth_login(request, user)
                return redirect('home')
        else:
            messages.error(request,login_form.errors)
    else:
        login_form = LoginForm()
    return render(request,'FormApp/login.html',{'login_form':login_form})

def logout(request):
    auth_logout(request)
    return  redirect('login')