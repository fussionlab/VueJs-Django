
# Build a Simple Blog application Using Django and VUE 
    
    Vue CLI and Django Reset framework

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
```zsh	  
  	$ mkdir Vue-Django
```	
Next, we will navigate into the directory:
```zsh
	 $ cd Vue-Django
```
Now we will install Pipenv using pip and activate a new virtual environment:
```zsh
 	$ pip install pipenv
 	$ pipenv shell
```
```Note: You should skip the first command if you already have Pipenv installed. If your using windows just add ```py py ``` instead of python```

Let’s install Django using Pipenv then create a new project called honeybee:
```zsh
  $ pipenv install django
  $ django-admin startproject honeybee
```
Next, we will navigate into the newly created backend folder and start a new application called todo. We will also run migrations and start up the server:
```zsh
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

```zsh 
$ python manage.py makemigrations blog
$ python manage.py migrate blog
```
You should see something similar to the following:

```py
Migrations for 'blog':
  blog/migrations/0001_initial.py:
    - Create model Post
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file blog/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.
for more details [Link](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

We can test to see that CRUD operations work on the Blog model we created using the admin interface that Django provides out of the box, but first, we will do a little configuration.

Open the blog/admin.py file and update it accordingly:
```py 
from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','created_on')
    list_filter = ('status',)
    search_fields = ['id','title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)
```
We will create a superuser account to access the admin interface with this command:
```zsh
$ python manage.py createsuperuser
``
   "You will be prompted to enter a username, email and password for the superuser. Be sure to enter details that you can remember because you will need them to log in to the admin dashboard shortly."
   
Let’s start the server once more and log in on the address — [http://localhost:8000/admin](http://localhost:8000/admin)
```zsh
$ python manage.py runserver
```
So far, we just done with admin! In the next section, we will see how we can create the API using the Django REST framework.

### Setting up the APIs

Now, we will quit the server (CONTROL-C or ctrl+c) then install the djangorestframework and django-cors-headers using Pipenv:
```zsh
$ pipenv install djangorestframework django-cors-headers
```
We need to add rest_framework and corsheaders to the list of installed applications, so open the honeybee/settings.py file and update the **INSTALLED_APPS** and **MIDDLEWARE** sections accordingly:
 ```py
 # settings.py

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',            # add this
        'rest_framework',         # add this 
        'blog',
      ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',    # add this
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
```
Add this code snippet to the bottom of the backend/settings.py file:
```py
    # we whitelist localhost:8080 because that's where frontend will be served
    CORS_ORIGIN_WHITELIST = (
         'localhost:8080/'
     )
```
Django-cors-headers is a python library that will help in preventing the errors that we would normally get due to CORS. rules. In the CORS_ORIGIN_WHITELIST snippet, we whitelisted localhost:8080 because we want the frontend (which will be served on that port) of the application to interact with the API.
Creating serializers for the Todo model

We need serializers to convert model instances to JSON so that the frontend can work with the received data easily. We will create a blog/serializers.py file:
```zsh
	$ touch blog/serializers.py
```
Open the serializers.py file and update it with the following code.
```py
    # blog/serializers.py
    from rest_framework import serializers
from .models import Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'slug', 'author','content','status','created_on')
```
In the code snippet above, we specified the model to work with and the fields we want to be converted to JSON.
### Creating the View

We will create a TodoView class in the blog/views.py file, so update it with the following code:
```py
    # blog/views.py
	from django.shortcuts import render

	# Create your views here.
	from rest_framework import viewsets       # add this
	from .serializers import BlogSerializer   # add this
	from .models import Post                  # add this

	class PostView(viewsets.ModelViewSet):       # add this
	    serializer_class =  BlogSerializer       # add this
	    queryset = Post.objects.all()  
```
The *viewsets* base class provides the implementation for CRUD operations by default, what we had to do was specify the serializer class and the query set.

Head over to the honeybee/urls.py file and completely replace it with the code below. This code specifies the URL path for the API:
```py
 # honeybee/urls.py

    from django.contrib import admin
    from django.urls import path, include                 # add this
    from rest_framework import routers                    # add this
    from blog import views                                # add this

    router = routers.DefaultRouter()                      # add this
    router.register(r'blog', views.TodoView, 'blog')     # add this

    urlpatterns = [
        path('admin/', admin.site.urls),         
	path('api/', include(router.urls))                # add this
    ]
```
This is the final step that completes the building of the API, we can now perform CRUD operations on the blog model. The router class allows us to make the following queries:

    /blog/ - This returns a list of all the Todo items (Create and Read operations can be done here).

    /blog/id - this returns a single Todo item using the id primary key (Update and Delete operations can be done here).

Let’s restart the server and visit this address — [http://localhost:8000/api/blog](http://localhost:8000/api/blog):
```zsh
$ python manage.py runserver
```
We can perform ADD, DELETE and UPDATE operations on specific Todo items using their id primary keys. To do this, we will visit an address with this structure /api/blog/id. Let’s try with this address — http://localhost:8000/blog/todos/1
Create a first post in /api/blog add slug if your *title* is like ***My first Post*** then slug should be like *my-first-post* 
