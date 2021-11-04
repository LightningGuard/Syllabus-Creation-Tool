from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [

    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('instructor', views.instructor, name='instructor'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('createSyllabus', views.createSyllabus, name='createSyllabus'),
    path('syllabusViewer', views.syllabusViewer, name='syllabusViewer'),
    path('addSyllabus', views.addSyllabus, name='addSyllabus'),


]