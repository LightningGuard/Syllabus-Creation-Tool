from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Custom User class (extensible fields)
class User(AbstractUser):
    pass

# Relationships
class SchoolList(models.Model):
    school_id = models.ManyToManyField('School')


class SyllabusList(models.Model):
    syllabus_id = models.ManyToManyField('Syllabus')

# USER TYPES
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # User Group 'Student'
    #sets type for student, null=True so that if it is not specified no error

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # User Group 'Instructor'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


#database for syllabus pdfs
class File(models.Model):
    syllabus_name = models.CharField(max_length=128, default='')  # TODO: Modify to connect to Syllabus table
    instructor_name = models.CharField(max_length=30, default='') # TODO: Modify to connect to Instructor table
    syllabus_file = models.FileField(upload_to='files')           # TODO: File system is a "weak database"

    def __str__(self):
        return self.syllabus_name

# Tables
class School(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=64, default='')
    zipcode = models.CharField(max_length=16, default='')
    syllabus_boilerplate = models.TextField(max_length=2056)


class Section(models.Model):
    section_id = models.CharField(max_length=8, default='')
    meeting_location = models.CharField(max_length=64, default='')
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    meeting_times = models.TextField(max_length=128, default='') # TODO: Meeting Times as Calendar data
    # calendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL())    # Setup for calendar meeting times


class Course(models.Model):
    course_name = models.CharField(max_length=128, default='')
    course_id = models.CharField(max_length=32, unique=True)
    course_description = models.TextField(max_length=512, default='')
    course_prereqs = models.TextField(max_length=256, default='')  # TODO: Set up built-in Course Pre-req references?
    # section_id = models.ForeignKey('Section'.section_id, on_delete=models.CASCADE) # TODO: fix field references


class Syllabus(models.Model):
    #### Course Info
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, null=True)
    #description = models.ForeignKey(Course.course_description, on_delete=models.CASCADE) #TODO: Fix field references

    # Teaching Assistants
    ta_blurb = models.TextField(max_length=512, default='')

    #### Course Materials
    course_materials_blurb = models.TextField(max_length=1024, default='')
    # Textbook
    # Other Readings
    # Lab Materials

    # Course Website (Standalone, Blackboard, etc.)
    course_website = models.URLField(max_length=256, default='')

    # Course Discussion forum (Discord, Piazza)
    course_discussion_blurb = models.TextField(max_length=512, default='')
    course_discussion_link = models.URLField(max_length=256, default='')

    # Academic Calendar
    # TODO: Pull from School.Calendar reference
    office_hours = models.TextField(max_length=256, default='')

    #### School Specific Dates (Pull from School.Calendar reference?)
    # Semester Start Date
    # sem_start_date = models.ForeignKey(School...)
    # Semester End Date
    # Drop/Add/Withdrawl Date
    # Holidays

    #### Section Specific Dates
    # Meeting Times
    #meeting_times_blurb = models.ForeignKey(Section.meeting_times) # TODO: Fix field references

    # Assignment Due Dates

    #### TODO: Grading - specific implementation of custom grading methods/calculations
    # Temp Grading text
    grading_blurb = models.TextField(max_length=1024, default='')

    # Boilerplate Language
    # Language From University
    #uni_boilerplate = models.ForeignKey(School.syllabus_boilerplate, on_delete=models.CASCADE) # TODO: Fix field references
    # Language From Department






