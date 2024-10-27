
# Build a Simple Blog application Using Django and VUE 
    
    Vue CLI and Django Reset framework

 ## Table of Contents

    #Prerequisites
    #Setting up the Backend(Honeybee)
    #Setting up the APIs
    #Setting up the frontend
    #Testing the application 
 
 ## In this tutorial, we will look at how to build a Simple Custom Blog using Django and Vue.

 ## Prerequisites

    To follow along with this tutorial, you will need the following installed on your machine:

        #Python.
        #Pip.
	#venv.
		
 ### Setting up the Backend

In this section, we will set up the backend and create all the folders that we need to get things up and running, so launch a new instance of a terminal and create the project’s directory and navigate by running this command:
##### Linux/Mac
```zsh	  
  	mkdir Vue-Django
	cd Vue-Django
```	
##### Windows
```powershell	
	mkdir Vue-Django
	cd Vue-Django
```
Now we will create virtual environment venv and activate a new virtual environment:
##### Linux/Mac
```zsh
 	python -m venv appenv
 	. appenv/bin/activate
```
##### Windows
```poweshell
	py -m venv appenv
	cd appenv/bin/
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
	./activate.ps1
	cd ../../
```

```Note: If your using windows just add ***py*** instead of python ```
#### For more detailed reference [Python venv](https://docs.python.org/3/tutorial/venv.html)
Let’s install Django using Pipenv then create a new project called honeybee:
##### Linux/Mac
```zsh
   pip install django
   django-admin startproject honeybee
```
##### Windows
```poweshell
	{: style="color:yellow"}pip install django
	django-admin startproject honeybee
```
Next, we will navigate into the newly created backend folder and start a new application called blog. We will also run migrations and start up the server:
##### Linux/Mac
```zsh
    cd honeybee
    python manage.py startapp blogs
    python manage.py migrate
    python manage.py runserver
````
##### Windows
```powershell
    cd honeybee
    py manage.py startapp blogs
    py manage.py migrate
    py manage.py runserver
````
At this point, if all the commands were entered correctly, we should see an instance of a Django application running on this address — http://localhost:8000

### For more detailed reference [Django Application](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

Registering the blog application

We are done with the basic setup for the honeybee, let’s start with the more advanced things like registering the honeybee application as an installed app so that Django can recognise it. Open the backend/settings.py file and update the INSTALLED_APPS section as so:
```python
    
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
 ```python	
 # blog/model.py 
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

##### Linux/Mac
```zsh 
	python manage.py makemigrations blogs
	python manage.py migrate blog
```
##### Windows
```powershell
	py manage.py makemigrations blogs
	py manage.py migrate blogs
```
You should see something similar to the following:

```shell
Migrations for 'blog':
  blog/migrations/0001_initial.py:
    - Create model Post
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file blog/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.
for more details [Link](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

We can test to see that CRUD operations work on the Blog model we created using the admin interface that Django provides out of the box, but first, we will do a little configuration.
### Adding controls to Admin
Open the ```blog/admin.py``` file and update it accordingly:
```python

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
##### Linux/Mac
```zsh
	python manage.py createsuperuser
```
##### Windows
```powershell
 	py manage.py createsuperuser
```
   "You will be prompted to enter a username, email and password for the superuser. Be sure to enter details that you can remember because you will need them to log in to the admin dashboard shortly."
   
Let’s start the server once more and log in on the address — [http://localhost:8000/admin](http://localhost:8000/admin)
##### Linux/Mac
```zsh
 python manage.py runserver
```
##### Windows
```powershell
	py manage.py runserver
```
So far, we just done with admin! In the next section, we will see how we can create the API using the Django REST framework.

### Setting up the APIs

Now, we will quit the server (CONTROL-C or ctrl+c) then install the djangorestframework and django-cors-headers using Pipenv:
##### Linux/Mac
```zsh
 	pip install djangorestframework django-cors-headers
```
##### Windows
```powershell
	pip install djangorestframework django-cors-headers
```
We need to add rest_framework and corsheaders to the list of installed applications, so open the honeybee/settings.py file and update the **INSTALLED_APPS** and **MIDDLEWARE** sections accordingly:
 ```python
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
```python
    # we whitelist localhost:8080 because that's where frontend will be served
    CORS_ORIGIN_WHITELIST = (
         'localhost:8080/'
     )
```
Django-cors-headers is a python library that will help in preventing the errors that we would normally get due to CORS. rules. In the CORS_ORIGIN_WHITELIST snippet, we whitelisted localhost:8080 because we want the frontend (which will be served on that port) of the application to interact with the API.

### Creating serializers for the blog model

We need serializers to convert model instances to JSON so that the frontend can work with the received data easily. We will create a ```blog/serializers.py``` file:
##### Linux/Mac
```zsh
	touch blog/serializers.py
```
##### Windows
```powershell
	New-Item -Path  "./blog/"  -Name "serializers.py"
```

Open the serializers.py file and update it with the following code.
```python
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

We will create a PostView class in the ```blog/views.py``` file, so update it with the following code:
```python
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

Head over to the ```honeybee/urls.py``` file and completely replace it with the code below. This code specifies the URL path for the API:
```python
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

    /blog/ - This returns a list of all the blog post (Create and Read operations can be done here).

    /blog/id - this returns a single blog post using the id primary key (Update and Delete operations can be done here).

Let’s restart the server and visit this address — [http://localhost:8000/api/blog](http://localhost:8000/api/blog):

##### Linux/Mac
```zsh
 	python manage.py runserver
```
##### Windows
```powershell
 	py manage.py runserver
```
***If want to run in diffrent port mean  ``` py manage.py runserver 8080```***
We can perform ADD, DELETE and UPDATE operations on specific blog post using their id primary keys. To do this, we will visit an address with this structure ```/api/blog/id```. Let’s try with this address — http://localhost:8000/blog/1
Create a first post in ```/api/blog``` add the slug field will be if your **title** is like ***My first Post*** then slug field should be like *my-first-post*.

## Setting up the frontend

We have our backend running as it should, now we will create our frontend and make it communicate with the backend over the interface that we created.

To install the vue/cli , in a terminal or command prompt type:
```zsh
 $ npm install -g @vue/cli
```
```zsh
 $ yarn add global @vue/cli
```
This may take a few minutes to install. You can now create a new Vue.js application by typing:
```bash
 $ vue create frontUI
```
where frontUI is the name of the folder for your application. You will be prompted to select a preset and you can keep the default (babel, eslint), which will use Babel to transpile the JavaScript to browser compatible ES5 and install the ESLint linter to detect coding errors. It may take a few minutes to create the Vue application and install its dependencies.

Let's quickly run our Vue application by navigating to the new folder and typing npm run serve to start the web server and open the application in a browser:
```zsh
 $ cd frontUI
 $ npm run serve 
```
You should see "Welcome to your Vue.js App" on http://localhost:8080 in your browser. You can press Ctrl+C to stop the vue-cli-service server.

we need to install bootstrap, bootstrap-vue, sass-loader and  node-sass

```zsh
 $ npm i bootstrap bootstrap-vue sass-loader node-sass --save
 ```
 Here i used both boostrap and bootstrap-vue, you can make your choice to use normal bootstrap or boostrap-vue. For detail reference [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) here bootstrap requires a peer of jquery@1.9.1-3 so install ```bash $ npm i jquery ``` and [Bootstrap-Vue](https://bootstrap-vue.js.org/docs/components/). We are going to use the SCSS or SASS so that sass-loader and node-sass complie scss for render.
 ### Setting App
 Open the ```src/App.vue``` you can see code as below:
 ```html
 <template>
  <div id="app">
     <img alt="Vue logo" src="./assets/logo.png">
      <HelloWorld msg="Welcome to Your Vue.js App"/> 
  </div>
</template>
<script>
 import HelloWorld from  './components/HelloWorld';
  export default {
    name: 'app',
    components: {
      HelloWorld
    }
  }

 </script>
<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>

 ```
 Here ``` <template> .... </template>``` holds all the markup and components, <HelloWorld /> is a component like this we can create as many as reuseable components. ```<script> ... </script> ``` holds javascripts like as ``` <style> ... </style>``` holds all inline stylesheat codes..
Next We are up to create Navigation bar component or Header and Footer

First we can create Navigation just commend as below:

```zsh
$ touch src/components/Navigation.vue
```

Now open the ```src/components/Navigation.vue``` write down as below:

```html
<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">Hornbill</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="p-2">
       <b-nav-item href="/blog">Blog</b-nav-item>
       <b-nav-item href="/about">About</b-nav-item>
     </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<script>
import {BNavbarNav, BNavItem, BNavbar, BNavForm,BFormInput, BNavItemDropdown,BDropdownItem, BNavbarBrand, BCollapse, BNavbarToggle, BButton} from 'bootstrap-vue';
export default {
    name:'Navi',
    components:{
        'b-navbar-brand':BNavbarBrand,
        'b-dropdown-item':BDropdownItem,
        'b-navbar':BNavbar,
        'b-nav-item':BNavItem,
        'b-collapse':BCollapse,
        'b-nav-item-dropdown':BNavItemDropdown,
        'b-nav-form':BNavForm,
        'b-navbar-toggle':BNavbarToggle,
        'b-button':BButton,
        'b-navbar-nav':BNavbarNav,
        'b-form-input':BFormInput,
    }
}
</script>
```
Here we used a bootstrap-vue components import all needed components from 'boostrap-vue' for the reference [https://bootstrap-vue.js.org/docs/components/navbar](https://bootstrap-vue.js.org/docs/components/navbar). you can use any navbar as you like.

Next create a footer of your choice here is my footer:

```zsh
$ touch src/components/footer.vue
```

Then open ```src/components/footer.vue``` and write code as below:

```html 
<template>
    <footer>
        <p><img alt="Vue logo" src="../assets/logo.png"> Hornbill Blog &copy; 2019</p>
    </footer>
</template>
<script>
export default {
    name:'AppFooter'
}
</script>
<style lang="scss">
footer{
    padding: 3rem;
    p{
        text-align: center;
        img{
            width:2rem;
        }
    }
}
</style>
```
Here we used a scss in our style as above.

Open the ```src/App.vue``` and add the components as below:
```html
 <template>
  <div id="app">
      <Navi />
         <img alt="Vue logo" src="./assets/logo.png">
      <AppFooter /> 
  </div>
</template>
<script>
 import Navi from  './components/Navigation';
 import AppFooter from  './components/footer';
  export default {
    name: 'app',
    components: {
      Navi,
      AppFooter,
    }
  }

 </script>
<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>

 ```
 Next we make a test run [http://localhost:8080](http://localhost:8080) :
 
 As we are creating a Blog, so that it needed to navigated to respective pages. We now use ```router``` to change single page app to multi page. Press ```Ctrl + c``` then command as below
 ```zsh
 $ npm i vue-router
 
 ```
 after install create a folder in `src/router` then
 
 ```zsh
 $ touch src/router/index.js
 ````
 
 Open the ```src/router/index.js``` file and write down the code as below:
 ```js
import Vue from 'vue'
import VueRouter from '../../node_modules/vue-router'
import Home from '../views/Home'
import Page from '../views/page/Page'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About')
  },
  {
     path: '/blog/:id', component: Page 
    
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

 ```
 On above you can see a components like `Home`, `About` and `Page` those are the components we going to create further. Create a folder in `src/views` manually or by command `$ mkdir views`. Then create files like `Home` and `About` just now.
 ```zsh
 	$ touch src/views/Home.vue
	$ touch src/views/About.vue
	$ touch src/views/page/Page.vue
```
Open Home and add one `<h1></h1>` tag in `template`
```html
<template>
	<h1>Home Page</h1>
<template>
<script>
	export default{
	name:'Home'
	}
</script>
```
Like create About and page for a test routing, add ```<h1>About Page</h1>``` on `About.vue` and ```<h1>Page</h1>``` on `page.vue`

Open the `App.Vue` and add following component 
```html
<template>
	<Navi />
	 <router-view/>
	<AppFooter />
</template>
```
The run [http://localhost:8080](http://localhost:8080) after command ,
```ash
  $ npm run serve
 ```
Then [http://localhost:8080/about](http://localhost:8080/about) to test routing, if you see the **About Page**. 

Next, proceding with connect to the `API` Before check you have add any blog post on `Django` or Press `Ctrl+c` and move to `honeybee` folder command
```zsh
 $ cd honeybee
 $ python manage.py runserver
```
Then run [http://localhost:8000/api/blog](http://localhost:8080/api/blog/) create the blog post after yo can see something like this
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
```json
[
    {
        "id": 1,
        "title": "Hello, world!",
        "slug": "hello-world",
        "author": 1,
        "content": "This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.\r\n\r\nIt uses utility classes for typography and spacing to space content out within the larger container.",
        "status": 1,
        "created_on": "2019-12-16T09:14:15.042351Z"
    }
]
````
Create posts as per your wish. Let this server run. In new terminal or command prompt type:
```zsh
$ npm i axios
```
Let it install and on time being we can add bootstrap to our style in `src/App.vue`
```html
<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap.scss';
@import 'assets/fontawesome/css/all.min.css';
</style>
``` 
This show how to use normal bootstrap and fontawesome (download the fontawesome manually form site.[Click here](https://fontawesome.com/download) got to downloading Page) on our code . Now check `axios` is installed.

Then open `src/view/Home.vue` and change the code as below:
```html
<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Blog Posts</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 p-1" v-for="(p, index) in items" :key="index">
        <div class="card">
          <img src="../assets/1.jpg" alt="" class="w-100" />
          <div class="card-body">
            <h4 class="card-title">{{ p.title }}</h4>
            <p class="card-text" v-if="p.content.length>100">{{ p.content.substring(0, 100)+ '...' }}</p>
            <a class="btn btn-primary text-light" >Read more</a>
          </div>
          <div class="card-footer">
            <ul>
              <li class="btn btn-default">
                 <i class="fa fa-heart text-danger"></i>0
              </li>
              <li class="btn btn-default" >
                <i class="fa fa-eye text-primary">0
              </li>
              <li value="2" class="btn btn-default">
               <i class="fa fa-comment text-success" ></i>0
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "home",
  data() {
    return {  
      items: [],
    };
  },
  
  mounted() {
    this.fetchItems();
    
  },
  methods: {
    fetchItems() {
      axios.get("http://localhost:8000/api/blog/").then(response => {
        this.items = response.data;
      });
    },
       
  }
};
</script>
<style lang="scss">
.col-md-6 {
  h4 {
    color: indigo;
  }
  .btn-circle {
    width: 40px;
    height: 40px;
    padding: 0.5rem;
    border-radius: 50%;
  }
  .btn {
    color: grey;
    span {
      color: grey;
    }
    .card {
      .card-footer {
        ul {
          list-style: none;
        }
        li{
          span{
            color: var(--dark)
          }
        }
        
        }
      }
    }
  }
}
</style>
```
Here `axios` fetch data from the `API` and make sure you a image on `assets/` folder here i got `assets/1.jpg`. To render `data(){}` function on `<template>` we use `{{some}}` here `some` is a sample data variable return forn *Data function* 
Example:
```html
<template>
	<h1>{{some}}</h1>
</template>
<script>
	export default{
	data(){
	return{
	some:'Sample Data',
	}
	}
	}
</script>
```
Above code is for example not for our code.

Here we in our app `v-for` is used to render all data(all the post) from the Api. `<div class="col-md-6 p-1" v-for="(p, index) in items" :key="index"> ...</div>` handel the loop.

`v-if` is used here to find the content is more then 100 letters display only 100 letters we going to use `substring()` function, `<p class="card-text"  v-if="p.content.length>100">{{ p.content.substring(0, 100)+ '...' }}</p>`. `<h4 class="card-title">{{ p.title }}</h4>` in this `{{p.title}}`  holds the title.

Now we have got all post form `Django` to our `Vue` App.

In Next section we can see how to get Total comments, Total View, Total likes and single Blog post view. We have to add three more model to our `Api`. Stop the both running servers by using `Ctrl+c`

Next go to the `Django` honeybee project. Open the `blog/model.py` and add this models to handel comments, reply, like, and views. 

```python

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
#add below  models Comment, Reply and Hits
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
class ReplyComment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
class Hitslike(models.Model):
      hitcount = models.IntegerField(default=0)
      viewcount = models.IntegerField(default=0)
      post = models.ForeignKey('Post', on_delete=models.CASCADE)
```
In the above `Comment` Model `post` is the foreignkey which stores the postid, Here we no need to specify `id` because `Django` create a default feild called `id`. Like that All three model have a relation with `Post` model. 

Then command 
```zsh
  $ python manage.py makemigrations
  $ python manage.py migrate
 ```
 Next, We can add serializers for reply, comment, and hitslike as below
 ```python
 
from rest_framework import serializers
from .models import Post, Comment, ReplyComment, Hitslike

#Serilaizer for Posts
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'slug', 'author','content','status','created_on')
	
#Serilaizer for Comments        
class CommentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','author','body','created_on','post')
	
#Serilaizer for Replys
class ReplyCommentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id','author','body','created_on','post','comment')
	
#Serilaizer for Views and Likes
class HitsLikeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Hitslike
        fields = ('id','hitcount','viewcount','post')
```
Save it, Next we add a view for all open `blog/views.py`

```python
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets      
from .serializers import BlogSerializer, CommentSerilaizer, ReplyCommentSerilaizer, HitsLikeSerilaizer    # add this
from .models import Post, Comment, ReplyComment, Hitslike   # add this

class PostView(viewsets.ModelViewSet):      
    serializer_class =  BlogSerializer      
    queryset = Post.objects.all()  
    
class CommentView(viewsets.ModelViewSet):  # add this
    serializer_class =  CommentSerilaizer      
    queryset = Comment.objects.all()  
    
    def get_queryset(self):
        qs = Comment.objects.all()  
        posts = self.request.query_params.get('post',None)
        
        if posts is not None:
            return qs.filter(post=posts) #return the comments /comment/?post=1
        return qs
	
class ReplyCommentView(viewsets.ModelViewSet): # add this
    serializer_class =  ReplyCommentSerilaizer       
    queryset = ReplyComment.objects.all()  
    
    def get_queryset(self):
        qs = ReplyComment.objects.all()  
        com = self.request.query_params.get('comment',None)
        pos = self.request.query_params.get('post', None)
        
        if pos is not None and com is not None:
            return qs.filter(post=pos,comment=com)
        elif pos is not None or com is not None:
            return qs.filter(post=pos)  
        return qs
	
class HitsLikesCountView(viewsets.ModelViewSet):  # add this
    serializer_class =  HitsLikeSerilaizer      
    queryset = Hitslike.objects.all()  
    
    def get_queryset(self):
        qs = Hitslike.objects.all()  
        pos = self.request.query_params.get('post',None)
        if pos is not None:
            return qs.filter(post=pos)
        return qs
```
Update your views like above. Next we can add links to those views in `honeybee/urls.py`, Open `urls.py` add

```python
"""honeybee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers                   
from blog import views                               
router = routers.DefaultRouter()                     
router.register(r'blog', views.PostView, 'post')     
router.register(r'comment', views.CommentView, 'comment')     # add this
router.register(r'replys', views.ReplyCommentView, 'replys')     # add this
router.register(r'hitlike', views.HitsLikesCountView, 'hitlike')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('api/', include(router.urls))                # add this
]
```
Next, Run the server ( Note: If you controls on admin you can add those to `admin.py` [Reference](https://github.com/fussionlab/vue-Django#add-controls-to-admin) repeat the step by adding models and fields to it)

```zsh
$ python manage.py runserver

```
Next section update the `Home.vue` to add likes count, comments count, and views count.
Open `src/views/Home.vue' add the following code to it.

```html
<template>
  <div class="home container">
    <div class="row">
      <div class="col-md-12">
        <h1>Blog Posts</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 p-1" v-for="(p, index) in items" :key="index">
        <div class="card">
          <img src="../assets/1.jpg" alt="" class="w-100" />
          <div class="card-body">
            <h4 class="card-title">{{ p.title }}</h4>
            <p class="card-text" v-if="p.content.length>100">{{ p.content.substring(0, 100)+ '...' }}</p>
            <!-- <span class="btn-circle btn-success" v-if="p.completed">&check;</span>
      <span class="btn-circle btn-warning" v-else>&cross;</span> -->
            <a v-on:click="ViewClick(p.id, hitlike[p.id-1].viewcount)"   class="btn btn-primary text-light" >Read more</a>
          </div>
          <div class="card-footer">
            <input type="hidden"  name="PostID"  :value='p.id' />
            <ul>
              <span v-for='hl in hitLikeFilter(p.id)' :key="hl.id">
              <li class="btn btn-default">
                 <i v-bind:class="DataCon(hl.hitcount)>=1?'fa fa-heart text-danger':'fa fa-heart'"></i><span> {{ hl.hitcount }}</span> 
              </li>
              <li class="btn btn-default" >
                <i  v-bind:class="DataCon(hl.viewcount)>=1?'fa fa-eye text-primary':'fa fa-eye'" class=""></i> <span>{{ hl.viewcount }}</span>
              </li>
              </span>
              <li value="2" class="btn btn-default">
               <i   v-bind:class="commentFilter(p.id).length>=1? 'fa fa-comment text-success':'fa fa-comment'" ></i><span> {{commentFilter(p.id).length}}</span>
              </li>
              <!-- <li class="btn btn-default" v-on:click="likeClick(p.bloglikes, p.title, p.slug, p.content, p.author)">
                <i class="fa fa-heart "></i> {{ hitLikeFilter(p.id) }}
              </li> --> 
            </ul>
          </div>
        </div>
      </div>
    </div>
   <div class="sidebar"></div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "home",
  data() {
    return {
      items: [], // store blog posts in array form
      comments:[], //store comments
      hitlike:[], //store view and likes
    };
  },
    
  mounted() {
    this.fetchItems();
    this.fetchCommentCount(); 
    this.fetchHitLike();
  },
  methods: {
    // Getting the blog post from api
    fetchItems() {
      axios.get("http://localhost:8000/api/blog/").then(response => {
        this.items = response.data;
      });
    },
   //Getting the comments counts from Api
    fetchCommentCount(){
      axios.get("http://localhost:8000/api/comment/")
      .then(response => {
        this.comments = response.data;
      });
    },
    // Get likes and views form the Api using axios 
    fetchHitLike(){
      axios.get("http://localhost:8000/api/hitlike/")
      .then(response => {
        this.hitlike = response.data;
      });
    },
    ViewClick: function(id,views) {
      const likecount = views + 1; 
      axios.put("http://localhost:8000/api/hitlike/"+ id +"/",{viewcount: likecount,post:id})
      .then(this.$router.push({ path: `/blog/${id}` }))
      .catch((response) => console.log('error', response));
    }, 
   //filter comments by it's post 
    commentFilter: function(id) {
      return this.comments.filter(el => {
        return el.post === id;
      })
    },
   //filter the  likes and views by it's post
    hitLikeFilter:function(hitlikeData){
      return this.hitlike.filter(el => {
        return el.post === hitlikeData;
     })
    },
    DataCon:(data)=>{
      return parseInt(data);
    },
  
  }
};
</script>
<style lang="scss">
.col-md-6 {
  h4 {
    color: indigo;
  }
  .btn-circle {
    width: 40px;
    height: 40px;
    padding: 0.5rem;
    border-radius: 50%;
  }
  .btn {
    color: grey;
    span {
      color: grey;
    }
    .card {
      .card-footer {
        ul {
          list-style: none;
        }
        li{
          span{
            color: var(--dark)
          }
        }
        span{
          li:nth-of-type(2){
          order: 3
        }
        
        }
      }
    }
  }
}
</style>

```
Next open the `src/App.vue` and modify the `style` tag code by adding colors to it.
```html
...
<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap.scss';
@import 'assets/fontawesome/css/all.min.css';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.bg-color-1 {background-color: #581845;}.bg-color-2 {background-color: #900C3F;}.bg-color-3 {background-color: #C70039;}.bg-color-4 {background-color: #FF5733;}.bg-color-5 {background-color: #FFC300;}.bg-color-6 {background-color:  #33691e ;}
.bg-color-7 {background-color: #3498db;}.bg-color-8 {background-color: #DAF7A6;}.bg-color-9 {background-color: #8e44ad;}.bg-color-10 {background-color: #34495e;}.bg-color-11 {background-color: #d35400;}.bg-color-12 {background-color: #2e86c1;}.bg-color-13{background-color:#e91e63}
.color-1 {color: #581845 !important;}.color-2 {color: #900C3F !important;}.color-3 {color: #C70039 !important;}.color-4 {color: #FF5733 !important;}.color-5 {color: #FFC300 !important;}.color-6 {color:  #33691e !important;} 
</style>
```
Here those `.bg-color` will be used in Avatar of Comments and Reply and there is font.

Next open the `views/page/page.vue` and update the code as below:
```html
<template>
  <div class="blog">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb container">
        <li class="breadcrumb-item"><a href="/">Home</a></li>
        <li class="breadcrumb-item"><a href="#">Blog</a></li>
        <li class="breadcrumb-item active" aria-current="page">
          {{ blogData.title }}
        </li>
      </ol>
    </nav>
    <div class="container">
      <div class="row">
        <div class="col-md-12 pt-1 pb-2">
          <h1>{{ blogData.title }}</h1>
        </div>
        <div class="col-md-12">
          <p class="m-2">{{ blogData.content }}</p>
          <div class="mt-5 mb-3 ml-3">
          <span class="text-md-right btn btn-default" v-on:click="LikeClick(blogData.id, likeValue() )"><i class="fa fa-heart"></i></span>
          </div>
         <section class="link-holder m-1 rounded">
           <ul class="clear-fix"> 
             <li>
               <h4 role="presentation">created</h4>
               <div class="topic-map-post created-at">
                 <a >
                   <b class="btn-sm rounded-circle m-sm-1 bg-warning text-white font-weight-light">C</b>
                 </a>
                   <span v-bind:title="blogData.created_on">{{formatDate(blogData.created_on )}}</span>
              </div>
             </li>
             <li>
               <a>
                  <h4 role="presentation">last {{commentLastDate() > replyLastDate()?'comment':replyLastDate()=== undefined?'comment':'reply'}}</h4>
                  <div class="topic-map-post last-reply">
                    <a class="trigger-user-card " data-user-card="ToddBroeker"> <b class="btn-sm rounded-circle m-sm-1 bg-info text-white font-weight-light">R</b></a>
                  <span >{{commentLastDate() > replyLastDate()?formatDate(commentLastDate()):replyLastDate()=== undefined?formatDate(commentLastDate()):commentLastDate()=== undefined?'No reply':formatDate(replyLastDate())}}</span>
                  </div>
                </a>
              </li>
              <li>
                <span class="number">{{blogComment.length}}</span>
                <h4 role="presentation">comments </h4>
              </li>
              <li>
                <span class="number">{{blogReply.length}}</span>
                <h4 role="presentation">replies</h4>
              </li>
              <span v-for="count in blogHitView" :key="count.id">
              <li class="secondary">
                <span class="number" title="3477" >{{count.viewcount}}</span>
                <h4 role="presentation">views</h4>
              </li>
              <li class="secondary">
                <span class="number" title="3477" >{{count.hitcount}}</span>
                <h4 role="presentation">likes</h4>
              </li>
              </span>
           </ul>
         </section>
        </div>
        <div class="col-md-12">
          <div class="comment">
            <!--Comments-->
            <div class="card card-comments mb-3 wow fadeIn">
              <div class="card-header font-weight-bold">
                {{ blogComment.length }} comments
              </div>
              <div class="card-body">
                <div
                  class="media d-block d-md-flex mt-4"
                  v-for="(c, Index) in blogComment"
                  :key="Index"
                >
                  <div :class="'avatar ' + AvatarColorChange(c.author.substring(0,1))"><h2 class="text-center pt-1 mt-md-1 mt-sm-2 mt-lg-1">{{c.author.substring(0,1).toUpperCase()}}</h2></div>
                  <div class="media-body text-center text-md-left ml-md-3 ml-0">
                    <h5 class="font-weight-bold"> {{ c.author }} <span class="relative-date float-right font-weight-lighter">{{formatDate(c.created_on)}}</span></h5>
                    <p>{{ c.body }} </p>
                    
                    
                    <div class="text-right pt-1">
                      <a id="reply" v-on:click="showModal(Index)">Replay</a>
                    </div>
                    <hr />
                    <div class="media d-block d-md-flex mt-3" v-for="reply in replyFilter(c.id)" :key="reply.id">
                    <div :class="'avatar ' + AvatarColorChange(reply.author.substring(0,1))"><h2 class="text-center pt-1 mt-md-1 mt-sm-2 mt-lg-1">{{reply.author.substring(0,1).toUpperCase()}}</h2></div>
                    <div class="media-body text-center text-md-left ml-md-3 ml-0">
                        <h5 class="mt-0 font-weight-bold">{{reply.author}} <span class="relative-date float-right font-weight-lighter">{{formatDate(reply.created_on)}}</span></h5>
                        <p>{{reply.body}}</p>
                    
                    <hr />
                    </div>
                   </div>
                   <ReplyModal :ref="'modal_' + Index">
                     <form @submit.prevent="replyPost(c.id)">
                      <label for="user">Your Name</label>
                      <input type="text" class="form-control" name="user" v-model="replyUser" required />
                      <input type="hidden" :value="c.id" :id="'commentid'+Index" :ref="'commentId'+Index" />
                      <label for="quickReplyFormComment">Your comment</label>
                      <textarea
                        class="form-control"
                        id="quickReplyFormComment"
                        rows="5" v-model="replyBody"
                        required
                      ></textarea>
                      <div class="mt-2 mb-2 float-right">
                        <button class="btn btn-info btn-sm" type="submit">
                          Post
                        </button>
                      </div>
                     </form>
                     </ReplyModal>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--/.Comments-->

            <!--Reply-->
            <div class="card mb-3 wow fadeIn">
              <div class="card-header font-weight-bold">Leave a Comment</div>
              <div class="card-body">
                <!-- Default form reply -->
                <form @submit="commentPost">
                  <!-- Name -->
                  <label for="replyFormName">Your name</label>
                  <input type="text"  id="replyFormName" v-model="commentAuthor" class="form-control" required />
                  <!-- Comment -->
                  <div class="form-group">
                    <label for="replyFormComment">Your comment</label>
                    <textarea class="form-control" id="replyFormComment" rows="5" required  v-model="commentBody"></textarea>
                  </div>
                  <div class="form-group">
                    <button class="btn btn-info btn-md mr-2" >Post</button>
                    <button class="btn btn-warning">Cancel</button>
                  </div>
                </form>
                <!-- Default form reply -->
              </div>
            </div>
            <!--/.Reply-->
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios';
import moment from 'moment';
import ReplyModal from './replyModal';
export default {
  
  name: "post",
  components:{
    ReplyModal
  },
  data() {
    return {
      blogData: {},
      blogComment:[],
      blogReply:[],
      blogHitView:{},
      commentBody:'',
      commentAuthor:'',
      replyUser:'',
      replyBody:'',
    };
  },
  mounted() {
    this.fetchBlogItems();
    this.fetchComment();
    this.formatDate();
    this.fetchHitLike();
    this.fetchReply();
    
  },
  computed: {
   
  },
  methods: {
    fetchBlogItems() {
      axios
        .get("http://localhost:8000/api/blog/" + this.$route.params.id + "/")
        .then(response => {
          this.blogData = response.data;
        });
    },
    fetchComment() {
      axios
        .get("http://localhost:8000/api/comment/?post=" + this.$route.params.id)
        .then(response => {
          this.blogComment = response.data;
        });
    },
    fetchHitLike(){
       axios
        .get("http://localhost:8000/api/hitlike/?post=" + this.$route.params.id)
        .then(response => {
          this.blogHitView = response.data;
        });
    },
    fetchReply(){
       axios
        .get("http://localhost:8000/api/replycomment/?post="+this.$route.params.id)
        .then(response => {
          this.blogReply = response.data;
        });
    },
    LikeClick: function(id,likes) {
      const likecount = parseInt(likes) + 1; 
      axios.put("http://localhost:8000/api/hitlike/"+ id +"/",{hitcount: likecount,post:id})
      .then( this.fetchHitLike())
      .catch((response) => console.log('error', response));
    }, 
    // Comment Post //
    commentPost:function(e){
      e.preventDefault();
        const item ={author:this.commentAuthor, body:this.commentBody, post:this.$route.params.id};
        axios.post("http://localhost:8000/api/comment/",item).then(location.reload()).catch(res => console.log('error', res))
      
    },   
    // Reply Filter //
    replyFilter: function(id) {
      return this.blogReply.filter(el => {
        return el.comment === id;
      })
    },
    //Reply Post
    replyPost:function(e){
       const item = {author:this.replyUser, body:this.replyBody, comment:e, post:this.$route.params.id}
       axios.post("http://localhost:8000/api/replycomment/",item).then(location.reload()).catch(res => console.log('error', res))
    },
     showModal(index) {
      let modal_id = "modal_" + index;
      this.$refs[modal_id][0].show();
    },
    // Formate Date //
    formatDate(value) {
      if (value) {
        return moment(String(value)).format('MMM DD')
      }
    },
    // LastDate Post
    commentLastDate() {
      var c = this.blogComment.length - 1;
      if(this.blogComment[c])
        return  this.blogComment[c].created_on;
    },
    replyLastDate(){
      var r = this.blogReply.length -1;
      if(this.blogReply[r])
        return this.blogReply[r].created_on;
    },
    likeValue(){
      var l =this.blogHitView.length -1
      if(this.blogHitView[l])
        return this.blogHitView[l].hitcount
    },
    //Avatar BG Colors
    AvatarColorChange(textExtract){
      const text = textExtract.toUpperCase();
      if(text ==='A'|text === 'B'){ return 'bg-color-1'; }
      else if(text === 'C' | text === 'D'){ return 'bg-color-2'; }
      else if(text === 'E' | text === 'F'){ return 'bg-color-3'; }
      else if(text === 'G' | text === 'H'){ return 'bg-color-4'; }
      else if(text === 'I' | text === 'J'){ return 'bg-color-5'; }
      else if(text === 'K' | text === 'L'){ return 'bg-color-6'; }
      else if(text === 'M' | text === 'N'){ return 'bg-color-7'; }
      else if(text === 'O' | text === 'P'){ return 'bg-color-8'; }
      else if(text === 'Q' | text === 'R'){ return 'bg-color-9'; }
      else if(text === 'S' | text === 'T'){ return 'bg-color-10'; }
      else if(text === 'U' | text === 'V'){ return 'bg-color-11'; }
      else if(text === 'W' | text === 'X'){ return 'bg-color-12'; }
      else if(text === 'Y' | text === 'Z'){ return 'bg-color-13'; }
      
    }
  }
};

</script>
<style lang="scss" >
.blog {
 @import '../../assets/scss/page';
}
</style>

```
Here the scss file is store in `assets/scss/` folder, there is a reply component is add to create it do as follow:
```zsh

 $ touch src/views/page/replyModel.vue
 
 ```
 Open the `replyModel.vue` and add code as below:
 ```html
 <template>
    <div class="form-group mt-4 fadeIn mb-3" v-if="visible">
     <button title="Close" class="btn btn-danger btn-sm float-right mb-1" @click='close()'>X</button>
          <slot></slot>
    </div>
</template>

<script>
export default {
    name:"ReplyModal",

    data(){
        return {
            visible : false
        }
    },
    methods : {
        show(){
            this.visible = true
        },
        close(){
            this.visible = false
        }
    }
}
</script>

 ```
This is an sample of reusable components, when reply text is clicked it will add this modal to our comment section. Here is the `page.scss` file code (create it on `/assets/scss` folder or `views/page/` any where you like but add the location correctly or else it through a runtime error.) 
```css



    nav {
      background-color: #5fcbdc;
      .breadcrumb {
        background-color: transparent;
      }
      a {
        color: #35495e;
      }
      a:hover {
        text-decoration: none;
      }
      h1 {
        padding-bottom: 1rem;
      }
      .active {
        color: white;
      }
     }
    section.link-holder{
      background-color: #f5f3f3;
      border:1px solid #e9e9e9;
      ul{
        list-style: none;
        li{
          float: left;
          padding: 7px 10px;
          h4{
            margin: 1px 0 2px 0;
            color: #919191;
            font-weight: normal;
            font-size: .8706em;
            line-height: 1;
           }
           .number {
            font-size: 1.3195em;
            line-height: 1.2;
          }
           .secondary {
            text-align: center;
          }
        }
        li:nth-child(3) {
          text-align: center;
       }
        }
      }
      .link-holder:first-of-type {
        display: flex;
    }
    
    .back {
      background-color: #42b883;
      color: white;
      margin-top: 5rem;
      text-decoration: none;
      padding: 10px 15px;
      border: 1px solid currentColor;
      border-radius: 0.5rem;
      display: inline-block;
      transition: all 0.3s ease;
      &:hover {
        background-color: transparent;
        color: #42b883;
      }
    }
    /deep/ {
      h1 {
        font-size: 3rem;
        margin-bottom: 0.2rem;
        color: #42b883;
      }
      h4 {
        margin-bottom: 3rem;
        color: #35495e;
      }
      p {
        white-space: pre-wrap;
        word-wrap: break-word;
        font-family: inherit;
      }
      pre {
        width: 100%;
        background-color: #35495e;
        color: white;
        border-radius: 0.3rem;
        padding: 1rem;
      }
      img {
        max-width: 100%;
      }
    }
    .comment {
      .avatar{
        width:55px;
        height: 55px;
        border-radius: 50%;
        h2{
          color:white;
        }
      }
      #reply {
        color: #42b883;
        cursor: pointer;
      }
      #reply:hover {
        text-decoration: none;
        color: #5fcbdc;
      }
      .display-none {
        display: none;
      }
      a{
        font-size:.75rem
      }
      span.relative-date {
        white-space: nowrap;
        font-size: medium;
        color: #919191;
        
    }
   }
```
`Note: Here ``/deep/`` on code doesn't support on chrome, ignore the warnings`
Save the file. Run the serve 
```zsh
$ npm run serve
```
`Note if django server is not running run that too..`

#### In next tutorial we can see how to add admin page and control the post from admin page.
