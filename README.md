# djangoTutorial
Project developed using Django 2.1.2 with Python3.6 in Eclipse 2018-2019, following the instructions in the online tutorial found at https://docs.djangoproject.com/en/2.1/intro/tutorial01/. This project consists of a simple poll application and is used to practice fundamental concepts in Django projects, from setting up the environment to developing models and querying the database.

# USER MANUAL

# DEVELOPER MANUAL
  -- PROCESS TO CONFIGURE DEVELOPER ENVIRONMENT (ASSUMING Ubuntu / Debian as OS and Eclipse, Python, Django versions as in the project description)
  1. Install virtualenv: $ pip install virtualenv 
  2. Go to folder in which the project will reside: $ cd /home/project/
  3. Create virtual environment using Python3.6: /home/project/$ virtualenv --python=python3.6 ./
     This assumes an environment variable in Ubuntu named "python3.6", if not set, you would have to provide the --python flag      with the full path to a python 3.6 interpreter (e.g. /usr/bin/python3.6)
  4. Activate virtual environment: /home/project/$ source bin/activate
  5. Install Django in virtual environment: (project) /home/project/$ pip install Django==2.1.2
  6. Create new directory with the same name as your project: (project) /home/project/$ mkdir project
  7. Go to Eclipse, copy an existing project or create new one as explained below.
  
  THIS ASSUMES YOU HAVE PyDev INSTALLED, if not, simply go to Eclipse marketplace (Help -> Eclipse marketplace), search and install PyDev
  
  -- PROCESS TO CREATE NEW PROJECT
  1. Select File -> New -> Other... Under PyDev options select PyDev Django project
  2. Name your project and under project contents unselect "Use default"
  3. Browse the directory you created in step 6 above (that is /home/project/project in the example)
  4. Click the link that says "Click here to configure an interpreter not listed"
  5. Select New...
  6. Give the interpreter the same name as your project (or whatever you like)
  7. Browse for the Python interpreter created with the virtual environment ( /home/project/bin/python3.6 )
  8. Select apply and close
  9. Select the newly created interpreter using the dropdown menu
  10. Select next and then again next to configure your database settings
  
  -- PROCESS TO CLONE EXISTING PROJECT
  1. Download zip from Github, unzip in project folder (/home/project/project)
  2. Select File -> New -> Other... Under PyDev options select PyDev Django project
  3. Name your project and under project contents unselect "Use default"
  4. Browse for the folder where you unzipped your project
  5. Click the link that says "Click here to configure an interpreter not listed"
  6. Select New...
  7. Give the interpreter the same name as your project
  8. Browse for the Python interpreter created with the virtual environment ( /home/project/bin/python3.6 )
  9. Select the newly created interpreter using the dropdown menu
  10. 
  
# ADDITIONAL NOTES
