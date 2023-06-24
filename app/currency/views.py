from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from currency.models import *


def home_view(request):
    return HttpResponse("<h1>Hello, World!</h1>")
    
