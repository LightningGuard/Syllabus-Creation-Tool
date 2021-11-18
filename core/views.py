
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import File
from .forms import FileForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def student(request):
    return render(request, 'student.html')

def instructor(request):
    return render(request, 'instructor.html')

def search_result(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        files = File.objects.filter(syllabus_name__contains=searched)
        return render(request, 'search_result.html',
                      {'searched':searched,
                       'files':files})
    else:
        return render(request, 'search_result.html')

def upload(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form':form
    })

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message,
            # this will be used for email checking we reload the page if email is invalid
            'badEmail': False,
            # these will be used if the user did not input data to be sent
            'noNameEntry': False,
            'noMessageEntry': False,
            # if the user makes it through sending then well change this to let them know
            'messageSent': False

        }

        print(data)

        # if name/email/message is empty well let the user know they forgot to write something!
        if not name:
            data['noNameEntry'] = True

        if not message:
            data['noMessageEntry'] = True

        # check if user inputs a valid email address if not reset page with badEmail variable true
        try:
            validate_email(email)
        except ValidationError:
            data['badEmail'] = True
            return render(request, 'contactUs.html', data)
        else:
            print("good email")

        # check if user forgot and reload telling them they did
        if data['noNameEntry'] or data['noMessageEntry']:
            return render(request, 'contactUs.html', data)

        # if all fields are correctly inputted prep email to be sent to user and our account
        message = 'User:' + name + '\n' + message + '\n\nUser Email: ' + email

        # send_mail(subject, message, from_email, recipient_list (must be a list or tuple), fail_silently=False)

        # send user a confirmation email for contacting us
        send_mail('Thank you for Contacting us', 'This is a confirmation email letting you know we have received your '
                                                 'message and will reach back to you shortly! Thank you!',
                  'SyllabusToolAcc@gmail.com', [email], fail_silently=False)

        # send our tool account an email with user inquiry
        send_mail(name, message, email, ['SyllabusToolAcc@gmail.com'], fail_silently=False)

        # our messages has been sent
        data['messageSent'] = True
        # if all is okay then we can re print the page with a thank you at the bottom
        return render(request, 'contactUs.html', data)

    # otherwise nothing happened and we show the user original page
    return render(request, 'contactUs.html')
  
def createSyllabus(request):
    return render(request, 'createSyllabus.html')

def syllabusViewer(request):
    # this is just checking if the request was under post which it should be since i made the method post
    # also it is getting the date from user input and setting it equal to the variables i made
    if request.method == 'POST':
        course_name = request.POST.get('course_name', ",")
        course_id = request.POST.get('course_id', ",")
        instructor_name = request.POST.get('prof_name', ",")
        instructor_email = request.POST.get('prof_email', ",")
        instructor_office = request.POST.get('prof_office', ",")
        instructor_days = request.POST.get('office_day', ",")
        instructor_hours = request.POST.get('office_hours', ",")
        ta_names = request.POST.get('ta_names', ",")
        ta_emails = request.POST.get('ta_emails', ",")
        meeting_times = request.POST.get('class_time', ",")
        meeting_days = request.POST.get('class_days', ",")
        course_description = request.POST.get('course_description', ",")
        course_pre_req = request.POST.get('course_pre_req', ",")
        course_topics = request.POST.get('course_topics', ",")
        course_requirements = request.POST.get('materials', ",")
        grading_type = request.POST.get('grading_type', ",")
        grading_value = request.POST.get('grading_value', ",")
        work = request.POST.get('work', ",")
        assignment_dates = request.POST.get('due_dates', ",")

        counter = 0
        counter1 = 0

        counter2 = 0
        counter3 = 0

        counter4 = 0
        counter5 = 0

        errorCounter = 0

        # all of these for loop are turning the data into a list so i can iterate through it through html and make it
        # also made counters so i compare if certain parts have more input than others
        # for example if you put more email's than ta's
        test = [work]
        for element in test:
            list = element.split(',')

        for e in list:
            counter4 = counter4 + 1

        test1 = [assignment_dates]
        for element1 in test1:
            list1 = element1.split(',')

        for d in list1:
            counter5 = counter5 + 1

        test2 = [grading_type]
        for element2 in test2:
            list2 = element2.split(',')

        for p in list2:
            counter2 = counter2 + 1

        test8 = [grading_value]
        for element8 in test8:
            list8 = element8.split(',')

        for h in list8:
             counter3 = counter3 + 1

        test4 = [ta_emails]
        print(ta_emails)
        for element4 in test4:
            list4 = element4.split(',')

        for r in list4:
            counter = counter + 1

        test5 = [ta_names]
        for element5 in test5:
            list5 = element5.split(',')

        for w in list5:
            counter1 = counter1 + 1

        test6 = [course_topics]
        for element6 in test6:
            list6 = element6.split(',')

        # will check if course name is empty
        course_name_empty = False
        if not course_name:
            course_name_empty = True
            errorCounter = errorCounter + 1

        # will check if course id is empty
        course_id_empty = False
        if not course_id:
            course_id_empty = True
            errorCounter = errorCounter + 1

        # will check if prof name is empty
        instructor_name_empty = False
        if not instructor_name:
            instructor_name_empty = True
            errorCounter = errorCounter + 1

        # will check if there is a @ in the prof email
        instructor_email_invalid = False
        if "@" not in instructor_email:
            instructor_email_invalid = True
            errorCounter = errorCounter + 1

        # will check if the prof email is empty
        instructor_email_empty = False
        if not instructor_email:
            instructor_email_empty = True
            errorCounter = errorCounter + 1

        # will check if the prof office location is empty
        instructor_office_empty = False
        if not instructor_office:
            instructor_office_empty = True
            errorCounter = errorCounter + 1

        # will check if the prof office days is empty
        instructor_days_empty = False
        if not instructor_days:
            instructor_days_empty = True
            errorCounter = errorCounter + 1

        # will check if the prof office hours is empty
        instructor_hours_empty = False
        if not instructor_hours:
            instructor_hours_empty = True
            errorCounter = errorCounter + 1

        # will check if the prof office hours has a -
        instructor_hours_invalid = False
        if "-" not in instructor_hours:
            instructor_hours_invalid = True
            errorCounter = errorCounter + 1

        # will check if the ta names are empty
        ta_names_empty = False
        if not ta_names:
            ta_names_empty = True
            errorCounter = errorCounter + 1

        # will check if the ta names has too many people compared to number of emails
        ta_names_more = False
        if counter1 > counter:
            ta_names_more = True
            errorCounter = errorCounter + 1

        # will check if the ta emails are empty
        ta_emails_empty = False
        if not ta_emails:
            ta_emails_empty = True
            errorCounter = errorCounter + 1

        # will check if the ta emails has @ included
        ta_emails_invalid = False
        for y in list4:
            if "@" not in y:
                ta_emails_invalid = True
                errorCounter = errorCounter + 1

        # will check if the ta emails has too many emails compared to number of people
        ta_emails_more = False
        if counter > counter1:
            ta_emails_more = True
            errorCounter = errorCounter + 1

        # will check if the meeting time is empty
        meeting_times_empty = False
        if not meeting_times:
            meeting_times_empty = True
            errorCounter = errorCounter + 1

        # will check if the meeting time has -
        meeting_times_invalid = False
        if "-" not in meeting_times:
            meeting_times_invalid = True
            errorCounter = errorCounter + 1

        # will check if the meeting days is empty
        meeting_days_empty = False
        if not meeting_days:
            meeting_days_empty = True
            errorCounter = errorCounter + 1

        # will check if the course topics is empty
        course_topics_empty = False
        if not course_topics:
            course_topics_empty = True
            errorCounter = errorCounter + 1

        # will check if the needed materials is empty
        course_requirements_empty = False
        if not course_requirements:
            course_requirements_empty = True
            errorCounter = errorCounter + 1

        # will check if the course description is empty
        course_description_empty = False
        if not course_description:
            course_description_empty = True
            errorCounter = errorCounter + 1

        # will check if the course pre-req is empty
        course_pre_req_empty = False
        if not course_pre_req:
            course_pre_req_empty = True
            errorCounter = errorCounter + 1

        # will check if the assignment type is empty
        grading_type_empty = False
        if not grading_type:
            grading_type_empty = True
            errorCounter = errorCounter + 1

        # will check if the assignment type has to many compared to grade value
        grading_type_more = False
        if counter2 > counter3:
            grading_type_more = True
            errorCounter = errorCounter + 1

        # will check if the grade value is empty
        grading_value_empty = False
        if not grading_value:
            grading_value_empty = True
            errorCounter = errorCounter + 1

        # will check if the grade value has to many compared to assignment type
        grading_value_more = False
        if counter3 > counter2:
            grading_value_more = True
            errorCounter = errorCounter + 1

        # will check if the assignment is empty
        work_empty = False
        if not work:
            work_empty = True
            errorCounter = errorCounter + 1

        # will check if the assignment has to many compared to due dates
        work_more = False
        if counter4 > counter5:
            work_more = True
            errorCounter = errorCounter + 1

        # will check if the due dates is empty
        assignment_dates_empty = False
        if not assignment_dates:
            assignment_dates_empty = True
            errorCounter = errorCounter + 1

        # will check if the due dates has to many compared to assignment
        assignment_dates_more = False
        if counter5 > counter4:
            assignment_dates_more = True
            errorCounter = errorCounter + 1

        # will check if the due dates has / included
        assignment_dates_invalid = False
        for p in list1:
            if "/" not in p:
                assignment_dates_invalid = True
                errorCounter = errorCounter + 1

        # these 3 line are combining the same index from two word into another list as the same index
        # this is for the html page so that the format looks nice for example so that
        # list2[HomeWork,Quizzes,Exam] & list8[10%,30%,60%] will create list12['HomeWork , 10%', 'Quizzes , 30%' , 'Exams , 60%']
        list10 = [' , '.join(z) for z in zip(list5, list4)]

        list11 = [' , '.join(x) for x in zip(list, list1)]

        list12 = [' , '.join(y) for y in zip(list2, list8)]

        # makes a reference in the html so that i can call here to use data that i need to display info
        data = {
            'course_name': course_name,
            'course_id': course_id,
            'prof_name': instructor_name,
            'prof_email': instructor_email,
            'instructor_office': instructor_office,
            'instructor_days': instructor_days,
            'instructor_hours': instructor_hours,
            'ta_info': list10,
            'meeting_times': meeting_times,
            'meeting_days': meeting_days,
            'course_description': course_description,
            'course_pre_req': course_pre_req,
            'course_topics': list6,
            'course_requirements': course_requirements,
            'course_work': list11,
            'grading': list12,
            'course_name_empty': course_name_empty,
            'course_id_empty': course_id_empty,
            'instructor_name_empty': instructor_name_empty,
            'instructor_email_invalid': instructor_email_invalid,
            'instructor_email_empty': instructor_email_empty,
            'instructor_office_empty': instructor_office_empty,
            'instructor_days_empty': instructor_days_empty,
            'instructor_hours_empty': instructor_hours_empty,
            'instructor_hours_invalid': instructor_hours_invalid,
            'ta_names_empty': ta_names_empty,
            'ta_emails_empty': ta_emails_empty,
            'meeting_times_empty': meeting_times_empty,
            'meeting_times_invalid': meeting_times_invalid,
            'meeting_days_empty': meeting_days_empty,
            'course_topics_empty': course_topics_empty,
            'course_requirements_empty': course_requirements_empty,
            'course_description_empty': course_description_empty,
            'course_pre_req_empty': course_pre_req_empty,
            'grading_type_empty': grading_type_empty,
            'grading_value_empty': grading_value_empty,
            'work_empty': work_empty,
            'assignment_dates_empty': assignment_dates_empty,
            'assignment_dates_invalid': assignment_dates_invalid,
            'ta_names_more': ta_names_more,
            'ta_emails_more': ta_emails_more,
            'ta_emails_invalid': ta_emails_invalid,
            'grading_type_more': grading_type_more,
            'grading_value_more': grading_value_more,
            'assignment_dates_more': assignment_dates_more,
            'work_more': work_more,
        }

        if errorCounter > 0:
            return render(request, 'createSyllabus.html', data)
        else:
            return render(request, 'syllabusViewer.html', data)

#will just redirect back to creatSyllabus but did not really use
def addSyllabus(request):
    return HttpResponseRedirect(reverse('createSyllabus'))


