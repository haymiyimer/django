from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from.models import Teacher
# Create your views here.
def codding(request):
    return render ( request ,'codding.html')
def new(request):
    return render ( request, 'new.html')
def student(request):
    student = Student.objects.all()

    return render (request,'student.html',{"student":student})
def teacher (request):
    teacher= Teacher.objects.all()
    return render(request,'teacher.html',{"teacher":teacher})
def insertstudents(request):
    return render(request,'insertstudents.html')