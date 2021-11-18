"# Syllabus-Creation-Tool"

Syllabus creation tool is a new tool for professors to engage their students to look at their syllabi. Professors will be able to post their syllabi into our database to be stored where students can access them through a drop down menu. The website will offer students to be able to select their current classes which will then take all the important dates and plot them on a calendar. The website will also offer a visual breakdown of the course’s grading policy. Syllabus creation tool will allow the users to be able to create accounts. Which will be a student and professor account with different permissions. Overall, this is a new tool so that students will actually look at the course syllabi since usually most students do not and this will provide students with information that they will care about.
  
  
Running the project:  
    1) Clone the project  
    2) Switch to the dev branch and pull  
    3) Download the .env from Discord and save it to the project root directory (where you git cloned)  
    4) If not using pycharm, create a venv and switch to it  
    

  Run in a terminal: 

  
    python -m pip install -r requirements.txt      
    python manage.py migrate  
    python manage.py runserver  
In order for the search to work in the student page, make sure you uploaded something in instructor page.


Testing the project: 
    1) Download as above (if haven't already.)  
    
   In a terminal:  
   
    2) python manage.py test  
