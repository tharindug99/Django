from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def say_hello(request):
    # return HttpResponse("Hello, World!")
        path = request.path 
        method = request.method 
        content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
                '''.format(path, method) 
        return HttpResponse(content)

def about(request):
    return HttpResponse("This is the about page.")
