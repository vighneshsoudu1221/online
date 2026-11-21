from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("hello wellcome")

def show(request):
    return HttpResponse("hi vikky");

def send(request):
    http_resp = render(request,"index.html")
    return http_resp
     



