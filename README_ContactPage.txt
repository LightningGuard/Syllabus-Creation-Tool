"# Syllabus-Creation-Tool - contact page"
For this iteration ive focused on creating an easy way to support outgoing notifications to our users for whatever our devs are creating at the time.
To do this ive taken an account for our developers to share in concern to the site and utilize gmails api and smtp to allow our devs to easily
utilize an email system as they wish. I wanted to create something that shows off this tool in practice and a practical fashion so for the site i made a contact us
which utilizes outgoing and incoming emails from our syllabustoolacc@gmail.com account this page allows a user to send some type of comment or inquiry to us and
the system will then send the user a confirmation email alongside sending us an email from their account telling us what they wrote.
error checking was done by utilizing python if statements within html code (really cool stuff) if and only if they input something in all fields
and a proper email address the system will send.


Running the project:
    1) Clone the project
    2) Switch to the dev branch and pull
    3) Download the .env from Discord and save it to the project root directory (where you git cloned)
    4) If not using pycharm, create a venv and switch to it

  Run in a terminal:

    python -m pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

    once done to access the contactUs page navigate in a browser
    to http://127.0.0.1:8000/contactUs

Testing the project:
    1) Download as above (if haven't already.)
    2) Download chromedriver 9.5 unzip and store in core (we already have it there if not)

   In a terminal:
    1) python -m pip install selenium
    2) python manage.py test

    this will go through three new tests specifically for contactUs page those being
    1)a test opening and entering valid input for name,email,and inquiry then clicking submit
    2)a test opening and not entering anything in the text fields then clicking submit (this will reload and show all three fields shows errors telling user to fill in all fields)
    3)a test opening the site and entering an invalid email address then clicking submit (this will show the user that they have messed up that field and must enter a valid address)

    These tests seem sufficient as entering anything in name and message is valid as long as there is something there which the 2nd test validates
    and then for our system to work we need a valid email address which the 3rd test makes sure that we have a proper system in place for email addresses

    This contact page wasn't the goal of this iteration, but it reveals that an email system our devs to use has been properly completed