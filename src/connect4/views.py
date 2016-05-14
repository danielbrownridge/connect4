from django.shortcuts import render

def index(request):
    template = 'connect4/index.html'
    response = render(request, template) 
    return response

def signup(request):
    template = 'connect4/signup.html'
    response = render(request, template)
    return response
