from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home ( request):
    return HttpResponse ("welcome")
def about(request):
    return HttpResponse ("about")
def shoplocation(request):
    return HttpResponse ("shop location ")
