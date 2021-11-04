from django.test import TestCase
from django.test import Client
from django.urls import reverse,resolve
from core.views import createSyllabus,syllabusViewer
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

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


class TestInstructorPage(TestCase):
    def test_InstructorUrl(self):
        response = client.get(reverse('instructor'))
        assert (response.status_code == 200)

    def test_InstructorTemplates(self):
        response = client.get(reverse('instructor'))
        assert (response.templates[0].name == 'instructor.html')
        assert (response.templates[1].name == 'base_generic.html')


class TestCreateSyllabusPage(TestCase):

    def test_CreateSyllabusUrl(self):
        url = reverse('createSyllabus')
        self.assertEquals(resolve(url).func, createSyllabus)

class TestSyllabusViewerPage(TestCase):

    def test_SyllabusViewerUrl(self):
        url = reverse('syllabusViewer')
        self.assertEquals(resolve(url).func, syllabusViewer)

#tested if the button i added redirects you to create syllabus
class TestInstructorPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/instructor')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/form/button').click()
        time.sleep(3)

#this will run through everything with correct data and then submit. Which will take you to the viewer page and display data
#in a syllabus format
class TestSyllabusMakerPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/createSyllabus')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/form/dev[2]/input').send_keys('FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/form/dev[8]/input').send_keys('tsmith28@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/form/dev[14]/input').send_keys('2-3:15')
        self.browser.find_element_by_xpath('/html/body/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/form/dev[26]/input').send_keys('Biological Science 4th edition (volume 2), Scott Freeman, Prentice Hall Publishers')
        self.browser.find_element_by_xpath('/html/body/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/form/dev[30]/input').send_keys('Must complete MATH 150 or MATH 155 or MATH 151 with a C grade or better')
        self.browser.find_element_by_xpath('/html/body/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/form/dev[36]/input').send_keys('Read chapter 1,Read chapter 2,Read chapter 3,Read chapter 4')
        self.browser.find_element_by_xpath('/html/body/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/form/dev[39]/button').click()
        time.sleep(5)


# this will just make the input bad and just refresh the page and show where/what the errors are
class TestSyllabusBadInput(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_info(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/createSyllabus')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/form/dev[2]/input').send_keys(
            'FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/form/dev[8]/input').send_keys('tsmith28umbc.edu')
        self.browser.find_element_by_xpath('/html/body/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/form/dev[14]/input').send_keys('23:15')
        self.browser.find_element_by_xpath('/html/body/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/form/dev[39]/button').click()
        time.sleep(5)

