from django.urls import path
from . import views  # Import views from the current directory


urlpatterns = [
    path('',views.home),  # Home page
    path('say_hello/',views.say_hello),  # Hello page
    path('about/',views.about),  # About page
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # Query Params
    path('getuser/', views.qryview, name='qryview'), 
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
]