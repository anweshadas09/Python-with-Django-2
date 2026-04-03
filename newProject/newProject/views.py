""" Controller of our whole structure """
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin

def home(request):
   return render(request, 'index.html')
def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')
def services(request):
    return HttpResponse("Services")