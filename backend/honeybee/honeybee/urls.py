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
from rest_framework import routers                    # add this
from blog import views                               # add this
router = routers.DefaultRouter()                      # add this
router.register(r'blog', views.PostView, 'post')     # add this
router.register(r'comment', views.CommentView, 'comment')     # add this
router.register(r'replycomment', views.ReplyCommentView, 'replycomment')     # add this
router.register(r'hitlike', views.HitsLikesCountView, 'hitlike')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('api/', include(router.urls))                # add this
]
