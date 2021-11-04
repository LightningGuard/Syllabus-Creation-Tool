from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


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



