from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse  ( "welcome to my home page")
def about(request):
    return HttpResponse ( "about")
def contact (request):
    return HttpResponse ("contact")