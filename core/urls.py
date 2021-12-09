from django.contrib import admin


from . import views
from django.conf import settings
from django.conf.urls.static import static
from core import views

from django.urls import path, include
from django.conf.urls import url

urlpatterns = [

    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('instructor', views.instructor, name='instructor'),

    path('search_result', views.search_result, name='search_result'),
    path('upload', views.upload, name='upload'),


    path('admin/', admin.site.urls),
  

    ################################
    #For logging in and registering#
    ################################ 

    path('login', views.loginPage, name='registration/login'),
    path('register', views.registerPage, name='registration/register'),

    ################################
    #End logging in and registering#
    ################################ 

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', views.profile, name='profile'),
    url(r'^auth/', include('social_django.urls', namespace='social')),


    path('contactUs', views.contactUs, name='contactUs'),
    path('createSyllabus', views.createSyllabus, name='createSyllabus'),
    path('syllabusViewer', views.syllabusViewer, name='syllabusViewer'),
    path('addSyllabus', views.addSyllabus, name='addSyllabus'),
    path('dueDates', views.dueDates, name='dueDates'),
    path('syllabusPDF', views.syllabusPDF, name='syllabusPDF'),
    path('roadMap', views.roadMap, name='roadMap'),

    # SyllabusCreateForm
    path('syllabus-creator', views.syllabus_create_view, name='syllabus_create_view'),
    path('syllabus-create-success', views.syllabus_create_success_view, name='syllabus_create_success_view'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


