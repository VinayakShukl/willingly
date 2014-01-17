__author__ = 'Aditya'

from django.shortcuts import render

def home(request):
    return render(request, "home.html")
