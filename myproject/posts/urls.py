from django.urls import path
from . import views # from this current package

urlpatterns = [
    path('', views.posts_list), # already in posts path as far as django is concerened
]

# django knows to look for vieews
