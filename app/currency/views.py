from django.shortcuts import render
from django.shortcuts import render
from django.http.response import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello, Django!</h1>")
