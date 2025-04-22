from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


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

def pathview(request, name, id): 
    return HttpResponse("Name:{} <br> UserID:{}".format(name, id))

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def showform(request):
     return render(request, "form.html")

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 