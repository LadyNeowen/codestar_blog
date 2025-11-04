from django.shortcuts import render
from django.http import HttpResponse

def blog_hello(request):
    return HttpResponse("Hello, blog!", content_type="text/plain; charset=utf-8")
# Create your views here.
