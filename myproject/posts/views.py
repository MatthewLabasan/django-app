from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # retrieve all objects. this is django orm. do most data manipulation here!!!
    return render(request, 'posts/posts_list.html', { 'posts': posts }) # this posts/posts_list is starting off with /templates. goes first to the project we are in's template directory, then searches for posts/posts_list.html

    # third param passes data to the posts_lists template

def post_page(request, slug):
    post = Post.objects.get(slug=slug) # get one post that matches slug
    return render(request, 'posts/post_page.html', { 'post': post })