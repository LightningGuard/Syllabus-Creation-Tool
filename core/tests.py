from django.test import TestCase
from django.test import Client
from django.urls import reverse

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

# this tests correct input in contact page
class TestContactPageCorrect(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('core/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_info(self):
        self.browser.get(( '%s%s' % (self.live_server_url, '/contactUs')))
        time.sleep(3)

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/input').send_keys('john doe')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/input').send_keys('goodEmail@gmail.com')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[3]/textarea').send_keys('test message')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[4]/input').click()
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

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/input').send_keys('')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/input').send_keys('')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[3]/textarea').send_keys('')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[4]/input').click()
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

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/input').send_keys('John doe')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/input').send_keys('bademail.com')
        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[3]/textarea').send_keys('test message')

        time.sleep(2)

        self.browser.find_element_by_xpath('/html/body/div[1]/form/div[4]/input').click()
        time.sleep(4)