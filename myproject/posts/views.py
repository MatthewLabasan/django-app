from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html') # this posts/posts_list is starting off with /templates. goes first to the project we are in's template directory, then searches for posts/posts_list.html
