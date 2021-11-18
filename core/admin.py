from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Instructor



admin.site.register(Student)
admin.site.register(Instructor)

# Register your models here.
