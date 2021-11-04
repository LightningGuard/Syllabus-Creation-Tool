from django.shortcuts import render
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def student(request):
    return render(request, 'student.html')


def instructor(request):
    return render(request, 'instructor.html')


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
