
# ```diff ! Build a Simple Blog application Using Django and VUE ```
    Vue and Django rest framework

 ## Table of Contents

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
```bash	  
  	$ mkdir Vue-Django
```	
Next, we will navigate into the directory:
```bash
	 $ cd Vue-Django
```
Now we will install Pipenv using pip and activate a new virtual environment:
```bash
 	$ pip install pipenv
 	$ pipenv shell
```
```Note: You should skip the first command if you already have Pipenv installed. If your using windows just add ```py py ``` instead of python```

Let’s install Django using Pipenv then create a new project called honeybee:
```bash
  $ pipenv install django
  $ django-admin startproject honeybee
```
Next, we will navigate into the newly created backend folder and start a new application called todo. We will also run migrations and start up the server:
```bash
    $ cd backend
    $ python manage.py startapp blog
    $ python manage.py migrate
    $ python manage.py runserver
````
At this point, if all the commands were entered correctly, we should see an instance of a Django application running on this address — http://localhost:8000

### For more detailed reference [Django Application](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

Registering the blog application

We are done with the basic setup for the honeybee, let’s start with the more advanced things like registering the honeybee application as an installed app so that Django can recognise it. Open the backend/settings.py file and update the INSTALLED_APPS section as so:
```py 
    # honeybee/settings.py

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog'  # add this line 
      ]
 ```     
### Defining the Blog model

 Let's create a model to define how the Blog items should be stored in the database, open the blog/models.py file and update it with this snippet: 
 ```py	# blog/model.py 
	from django.db import models
	from django.contrib.auth.models import User

	STATUS = (
	    (0,"Draft"),
	    (1,"Publish")
	)

	class Post(models.Model):
	    title = models.CharField(max_length=200, unique=True)
	    slug = models.SlugField(max_length=200, unique=True)
	    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
	    updated_on = models.DateTimeField(auto_now= True)
	    content = models.TextField()
	    created_on = models.DateTimeField(auto_now_add=True)
	    status = models.IntegerField(choices=STATUS, default=0)

	    class Meta:
		ordering = ['id']

	    def __str__(self):
		return self.title
```
The code snippet above describes seven properties on the Blog model:

    Title
    Sulg
    Author
    Updated Date
    Content
    Created Date
    Status
    
  Slug is url for the post by the reference of it's title and Status is for save as draft or publish the post

```bash 
$ python manage.py makemigrations blog
$ python manage.py migrate blog
```
You should see something similar to the following:

```pr
Migrations for 'blog':
  blog/migrations/0001_initial.py:
    - Create model Post
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file blog/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.
for more details [Link](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

We can test to see that CRUD operations work on the Blog model we created using the admin interface that Django provides out of the box, but first, we will do a little configuration.

Open the blog/admin.py file and update it accordingly:
```
