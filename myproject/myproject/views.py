# from django.http import HttpResponse
from django.shortcuts import render
    # render is similar to HttpResponse in that it allows template usage, inputs dynamic data, then returns an HttpResponse object.

def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html') # django knows where this template is!

    # if you have dynamic data, you can pass it in here as (request, template, context={'variable': 'data'})
def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html') 