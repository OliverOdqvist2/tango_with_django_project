from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango say here there partner!")