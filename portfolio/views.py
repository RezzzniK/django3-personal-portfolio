from django.shortcuts import render
#IMPORTING models
from .models import Project

# Create your views here.
def home(request):
    #grabbing all object from db:
    projects=Project.objects.all()

    return render(request,'portfolio/home.html',#passing objects with request
                                                {'projects':projects} )
