from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import File
admin.site.register(User, UserAdmin)

# Register your models here.
class Syllabus(admin.ModelAdmin):
    list_display = ['syllabus_name','instructor_name','syllabus_file']

admin.site.register(File,Syllabus)
