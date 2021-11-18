from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    #sets type for student, null=True so that if it is not specified no error
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    Student_ID = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Instructor(models.Model):
    #sets type for teacher, null=True so that if it is not specified no error
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    Instructor_ID = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Custom User class (extensible fields)
class User(AbstractUser):
    pass


class Section(models.Model):
    section_id = models.CharField(max_length=8)
    meeting_location = models.CharField(max_length=64)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # meeting_times = models.CharField(max_length=64)                        # Meeting times as a string of text
    # calendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL())    # Setup for calendar meeting times


class Course(models.Model):
    course_name = models.CharField(max_length=128)
    course_id = models.CharField(max_length=32, unique=True)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)

#database for syllabus
class File(models.Model):
    syllabus_name = models.CharField(max_length=128)
    instructor_name = models.CharField(max_length=30)
    syllabus_file = models.FileField(upload_to='files')
    def __str__(self):
        return self.syllabus_name


# TODO: Syllabus setup as a custom filetype that we link and open here?
class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Course Materials
        # Textbook
        # Other Readings
        # Lab Materials
        # Course Website (Standalone, Blackboard, etc.)
        # Course Discussion forum (Discord, Piazza)
    # Academic Calendar
        # Semester Start Date
        # Semester End Date
        # Drop/Add/Withdrawl Date
        # Holidays
    # Course Calendar
        # Meeting Times - ** Handled in Course **
        # Assignment Due Dates
    # Boilerplate Language
        # Language From University
        # Language From Department
    pass



