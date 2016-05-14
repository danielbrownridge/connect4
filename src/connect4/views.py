#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = 'Connect4'
    response = HttpResponse(message)
    return response
