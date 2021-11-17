from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def student(request):
    return render(request, 'student.html')

def instructor(request):
    return render(request, 'instructor.html')