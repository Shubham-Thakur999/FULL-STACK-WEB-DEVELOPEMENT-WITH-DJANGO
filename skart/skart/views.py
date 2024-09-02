#we need to create this "views.py" page as it is not present itself.

#and below some part of code we have copied from "views.py" page of (shop) page.

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    # as discussed in earlier cases also ,this (index)function takes us to (index.html) page of our (skart) project.