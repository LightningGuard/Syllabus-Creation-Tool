from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Instructor, Syllabus, Course
from core.models import User


from .models import File
admin.site.register(User, UserAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_name']


class SyllabusFile(admin.ModelAdmin):
    list_display = ['syllabus_name', 'instructor_name', 'syllabus_file']


class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_name', 'instructor_name', 'instructor_email']

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(File, SyllabusFile)
