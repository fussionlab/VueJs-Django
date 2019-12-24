
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

Open the ```blog/admin.py``` file and update it accordingly:
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
```
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

### Creating serializers for the blog model

We need serializers to convert model instances to JSON so that the frontend can work with the received data easily. We will create a ```blog/serializers.py``` file:
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

We will create a PostView class in the ```blog/views.py``` file, so update it with the following code:
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

Head over to the ```honeybee/urls.py``` file and completely replace it with the code below. This code specifies the URL path for the API:
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

    /blog/ - This returns a list of all the blog post (Create and Read operations can be done here).

    /blog/id - this returns a single blog post using the id primary key (Update and Delete operations can be done here).

Let’s restart the server and visit this address — [http://localhost:8000/api/blog](http://localhost:8000/api/blog):

```zsh
$ python manage.py runserver
```

We can perform ADD, DELETE and UPDATE operations on specific blog post using their id primary keys. To do this, we will visit an address with this structure ```/api/blog/id```. Let’s try with this address — http://localhost:8000/blog/1
Create a first post in ```/api/blog``` add the slug field will be if your **title** is like ***My first Post*** then slug field should be like *my-first-post*.

## Setting up the frontend

We have our backend running as it should, now we will create our frontend and make it communicate with the backend over the interface that we created.

To install the vue/cli , in a terminal or command prompt type:
```zsh
 $ npm install -g @vue/cli
```
This may take a few minutes to install. You can now create a new Vue.js application by typing:
```bash
 $ vue create frontUI
```
where frontUI is the name of the folder for your application. You will be prompted to select a preset and you can keep the default (babel, eslint), which will use Babel to transpile the JavaScript to browser compatible ES5 and install the ESLint linter to detect coding errors. It may take a few minutes to create the Vue application and install its dependencies.

Let's quickly run our Vue application by navigating to the new folder and typing npm run serve to start the web server and open the application in a browser:
```bash
 $ cd frontUI
 $ npm run serve
```
You should see "Welcome to your Vue.js App" on http://localhost:8080 in your browser. You can press Ctrl+C to stop the vue-cli-service server.

we need to install bootstrap, bootstrap-vue, sass-loader and  node-sass

```bash
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

```bash
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

```bash 
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
 ```bash
 $ npm i vue-router
 
 ```
 after install create a folder in `src/router` then
 
 ```bash
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
 ```bash
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
```bash 
  $ npm run serve
 ```
Then [http://localhost:8080/about](http://localhost:8080/about) to test routing, if you see the **About Page**. 

Next, proceding with connect to the `API` Before check you have add any blog post on `Django` or Press `Ctrl+c` and move to `honeybee` folder command
```bash
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
```bash
$ npm i axios
```
Let it install and on time being we can add bootstrap to our style in `src/App.vue`
```html
<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap.scss';
</style>
``` 
This show how to use normal bootstrap on our code. Now check `axios` is installed.

Then open `src/view/Home.vue` and change the code as below:
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

`v-if` is used here to find the content is more then 100 letters display only 100 letters we going to use `substring()` function, `<p class="card-text" v-if="p.content.length>100">{{ p.content.substring(0, 100)+ '...' }}</p>`. `<h4 class="card-title">{{ p.title }}</h4>` in this `{{p.title}}` holds the title.

Now we have got all post form `Django` to our `Vue` App.

In Next section we can see how to get Total comments, Total View and Total likes. We have to add three more model to our `Api`
