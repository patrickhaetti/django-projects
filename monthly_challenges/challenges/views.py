from django.http import HttpResponse
from django.shortcuts import render

def january(request):
    return HttpResponse("<h1>Hello january</h1>")

def february(request):
    return HttpResponse("<h1>Hello february</h1>")