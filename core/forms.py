from django import forms
from .models import File, Syllabus

################################
#For logging in and registering#
################################ 

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #Here specify any information we want to take from user. In documentation
        fields = ['email', 'password1', 'password2']


# class CreateStudentForm(UserCreationForm):
#     class Meta:
#         model = Student
#         fields = []
    

# class CreateInstructorForm(UserCreationForm):
#     class Meta: 
#         model = Instructor
#         fields = '__all__'


################################
#End logging in and registering#
################################ 


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('syllabus_name', 'instructor_name', 'syllabus_file')

class SyllabusCreateForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        exclude = ['created_by']