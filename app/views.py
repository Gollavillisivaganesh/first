from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def geetha(request):
    return HttpResponse('<h1><marquee>Life is full of suprises and miracals</h1></marquee>')

def siva(request):
    return HttpResponse('<h1><marquee>create your own rules</h1></marquee>')
