from django.shortcuts import render
from django.http import HttpResponse
from .models import File


def index(request):
    return render(request, 'index.html')


def student(request):
    return render(request, 'student.html')


def instructor(request):
    return render(request, 'instructor.html')

def search_result(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        files = File.objects.filter(syllabus_name__contains=searched)
        return render(request, 'search_result.html',
                      {'searched':searched,
                       'files':files})
    else:
        return render(request, 'search_result.html')

