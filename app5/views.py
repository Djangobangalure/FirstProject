from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def hello(request):
    return HttpResponse('p<h1><marquee>python Class<marquee></h1> ')
