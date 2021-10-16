from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def frontpage(request):
    return render(request, 'core/home.html')

def signup(request):
    return render(request, 'core/signup.html')