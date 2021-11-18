from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Instructor



from .models import File
admin.site.register(User, UserAdmin)

admin.site.register(Student)
admin.site.register(Instructor)

# Register your models here.
class Syllabus(admin.ModelAdmin):
    list_display = ['syllabus_name','instructor_name','syllabus_file']

admin.site.register(File,Syllabus)
