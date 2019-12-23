# Build a Simple Blog application Using Django and VUE
    Vue and Django rest framework

 # Table of Contents

    #Prerequisites
    #Setting up the Backend
    #Setting up the APIs
    #Setting up the frontend
    #Testing the application 
 
 ## In this tutorial, we will look at how to build a Simple Custom Blog using Django and Vue.

 ## Prerequisites

    To follow along with this tutorial, you will need the following installed on your machine:

        #Python.
        #Pip.
        #Pipenv.
		
 ### Setting up the Backend

In this section, we will set up the backend and create all the folders that we need to get things up and running, so launch a new instance of a terminal and create the project’s directory by running this command:
	  
  $ mkdir Vue-Django
	
Next, we will navigate into the directory:

 $ cd Vue-Django

Now we will install Pipenv using pip and activate a new virtual environment:

 $ pip install pipenv
 $ pipenv shell

```Note: You should skip the first command if you already have Pipenv installed.```

Let’s install Django using Pipenv then create a new project called honeybee:

  $ pipenv install django
  $ django-admin startproject honeybee

Next, we will navigate into the newly created backend folder and start a new application called todo. We will also run migrations and start up the server:

    $ cd backend
    $ python manage.py startapp honeybee
    $ python manage.py migrate
    $ python manage.py runserver

At this point, if all the commands were entered correctly, we should see an instance of a Django application running on this address — http://localhost:8000

