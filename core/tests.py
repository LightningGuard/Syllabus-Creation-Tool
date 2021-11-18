from django.test import TestCase
from django.test import Client
from django.urls import reverse

client = Client()


class TestIndexPage(TestCase):
    def test_IndexUrl(self):
        response = client.get(reverse('index'))
        assert (response.status_code == 200)

    def test_IndexTemplates(self):
        response = client.get(reverse('index'))
        assert (response.templates[0].name == 'index.html')
        assert (response.templates[1].name == 'base_generic.html')


class TestStudentPage(TestCase):
    def test_StudentUrl(self):
        response = client.get(reverse('student'))
        assert (response.status_code == 200)

    def test_StudentTemplates(self):
        response = client.get(reverse('student'))
        assert (response.templates[0].name == 'student.html')
        assert (response.templates[1].name == 'base_generic.html')

    def test_searchResult(self):
        response = client.get(reverse('search_result'))
        assert (response.templates[0].name == 'search_result.html')
        assert (response.templates[1].name == 'base_generic.html')


class TestInstructorPage(TestCase):
    def test_InstructorUrl(self):
        response = client.get(reverse('instructor'))
        assert (response.status_code == 200)

    def test_InstructorTemplates(self):
        response = client.get(reverse('instructor'))
        assert (response.templates[0].name == 'instructor.html')
        assert (response.templates[1].name == 'base_generic.html')

    def test_upload(self):
        response = client.get(reverse('upload'))
        assert (response.templates[0].name == 'upload.html')
        assert (response.templates[1].name == 'base_generic.html')
