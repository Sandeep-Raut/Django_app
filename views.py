from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello world, I am Sandeep Anna Raut , from T3 batch , and my PRN is 1841045 .")