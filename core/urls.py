from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('instructor', views.instructor, name='instructor'),

    path('admin/', admin.site.urls),
  
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', views.profile, name='profile'),
    url(r'^auth/', include('social_django.urls', namespace='social')),

]