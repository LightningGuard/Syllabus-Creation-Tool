from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import File
from .forms import FileForm
from django.core.files.storage import FileSystemStorage

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

def upload(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form':form
    })