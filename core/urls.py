from django.contrib import admin
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from core import views


urlpatterns = [

    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('instructor', views.instructor, name='instructor'),
    path('search_result', views.search_result, name='search_result'),
    path('upload', views.upload, name='upload'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('createSyllabus', views.createSyllabus, name='createSyllabus'),
    path('syllabusViewer', views.syllabusViewer, name='syllabusViewer'),
    path('addSyllabus', views.addSyllabus, name='addSyllabus'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

