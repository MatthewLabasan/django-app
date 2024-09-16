from django.urls import path
from . import views # from this current package

urlpatterns = [
    path('', views.posts_list, name="posts"), # already in posts path as far as django is concerened
    path('<slug:slug>', views.post_page, name="page"), # already in posts path as far as django is concerened
]

# django knows to look for views
# we add a name to the url so we can refer to it in our template files for url embedding. 
# this will allow us to add params to it as well

# <> path converter; inside is type of path converter, and after : is the param we are passing in -- in this, our slig
