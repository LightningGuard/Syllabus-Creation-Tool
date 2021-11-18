from django import forms
from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('syllabus_name', 'instructor_name', 'syllabus_file')