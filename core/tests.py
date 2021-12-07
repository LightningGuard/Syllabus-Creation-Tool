from django.test import TestCase
from django.test import Client
from django.urls import reverse,resolve
from core.views import createSyllabus,syllabusViewer,dueDates,syllabusPDF
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

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


class TestCreateSyllabusPage(TestCase):

    def test_CreateSyllabusUrl(self):
        url = reverse('createSyllabus')
        self.assertEquals(resolve(url).func, createSyllabus)

class TestSyllabusViewerPage(TestCase):

    def test_SyllabusViewerUrl(self):
        url = reverse('syllabusViewer')
        self.assertEquals(resolve(url).func, syllabusViewer)

class TestCalendarPage(TestCase):

    def test_SyllabusViewerUrl(self):
        url = reverse('dueDates')
        self.assertEquals(resolve(url).func, dueDates)

class TestPDFPage(TestCase):

    def test_SyllabusViewerUrl(self):
        url = reverse('syllabusPDF')
        self.assertEquals(resolve(url).func, syllabusPDF)

# will check if the button on the student page redirects them
class TestCalendarPageLive(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/student')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form[2]/button').click()
        time.sleep(3)

#tested if the button i added redirects you to create syllabus
class TestInstructorPageLive(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/instructor')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/button').click()
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
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[2]/input').send_keys('FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[8]/input').send_keys('randomemail@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[14]/input').send_keys('2-3:15')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[26]/input').send_keys('Biological Science 4th edition (volume 2), Scott Freeman, Prentice Hall Publishers')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[30]/input').send_keys('Must complete MATH 150 or MATH 155 or MATH 151 with a C grade or better')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[36]/input').send_keys('Read chapter 1,Read chapter 2,Read chapter 3,Read chapter 4')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        time.sleep(3)


        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/button[1]').click()


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

        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[2]/input').send_keys(
            'FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[8]/input').send_keys('randomemailumbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[14]/input').send_keys('23:15')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        time.sleep(3)



        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/button[1]').click()


        time.sleep(5)


# this tests correct input in contact page
class TestContactPageCorrect(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_info(self):
        self.browser.get(( '%s%s' % (self.live_server_url, '/contactUs')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[1]/input').send_keys('john doe')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[2]/input').send_keys('goodEmail@gmail.com')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[3]/textarea').send_keys('test message')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[4]/input').click()
        time.sleep(4)
        
# this tests if there is no input in the fields contact page
class TestContactPageNoInput(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_info(self):
        self.browser.get(( '%s%s' % (self.live_server_url, '/contactUs')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[1]/input').send_keys('')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[2]/input').send_keys('')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[3]/textarea').send_keys('')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[4]/input').click()
        time.sleep(4)

# This method tests invalid email input only contact page
class TestContactPageInvalidEmail(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_info(self):
        self.browser.get(( '%s%s' % (self.live_server_url, '/contactUs')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[1]/input').send_keys('John doe')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[2]/input').send_keys('bademail.com')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[3]/textarea').send_keys('test message')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/div[1]/form/div[4]/input').click()
        time.sleep(4)


# this test will just check the new syllabus page with the boiler plate options only clicked 2 out of 3 boxes
class TestSyllabusMakerPageWithNewInput(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/createSyllabus')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[2]/input').send_keys('FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[8]/input').send_keys('randomemail@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[14]/input').send_keys('2-3:15')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[26]/input').send_keys('Biological Science 4th edition (volume 2), Scott Freeman, Prentice Hall Publishers')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[30]/input').send_keys('Must complete MATH 150 or MATH 155 or MATH 151 with a C grade or better')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[36]/input').send_keys('Read chapter 1,Read chapter 2,Read chapter 3,Read chapter 4')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[43]/input').click()
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[45]/input').click()
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/button[1]').click()

        time.sleep(5)

#will check if the functionality of the page works. Also, the 3rd day box is grey which means that it is being hovered
class TestCalendarFunctionality(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/dueDates')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[28]').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/input').send_keys('CMSC 421 Hw5 Due & CMSC 411 Exam')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/button[1]').click()
        time.sleep(5)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[32]').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/input').send_keys('CMSC 447 Hw5 Due')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/button[1]').click()
        time.sleep(5)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[14]').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/input').send_keys('CMSC 426 Hw7 Due')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/button[1]').click()
        time.sleep(5)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[15]').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/input').send_keys('CMSC 447 Exam')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/button[1]').click()
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/button').click()
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button').click()
        time.sleep(3)


class TestPDFPageLive(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()


    def test_work(self):
        self.browser.get(('%s%s' % (self.live_server_url, '/createSyllabus')))
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[2]/input').send_keys('FOUNDATIONS OF BIOLOGY II: ECOLOGY & EVOLUTION')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[4]/input').send_keys('BIOL 142')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[6]/input').send_keys('Tony Smith')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[8]/input').send_keys('randomemail@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[10]/input').send_keys('Ite 203')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[12]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[14]/input').send_keys('2-3:15')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[16]/input').send_keys('Joseph Young,Zoe Morgan,Jennifer Gill')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[18]/input').send_keys('jyoung2@umbc.edu,mjenn10@umbc.edu,jgill2@umbc.edu')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[20]/input').send_keys('4-5:45')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[22]/input').send_keys('M/W')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[24]/input').send_keys('Natural Selection,Genetics,Speciation,Phylogeny')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[26]/input').send_keys('Biological Science 4th edition (volume 2), Scott Freeman, Prentice Hall Publishers')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[28]/input').send_keys('The goal of this course is to present an important series of topics in organismal biology ')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[30]/input').send_keys('Must complete MATH 150 or MATH 155 or MATH 151 with a C grade or better')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[32]/input').send_keys('Homework,Exam,Quiz')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[34]/input').send_keys('10%,60%,30%')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[36]/input').send_keys('Read chapter 1,Read chapter 2,Read chapter 3,Read chapter 4')
        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/dev[38]/input').send_keys('07/16,07/22,07/26,07/28')
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/center/div[2]/form/button[2]').click()

        time.sleep(5)


