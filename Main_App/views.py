from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

 #The home url function
def home(request):
    return render(request, 'home.html', {'name':'Shampi'})

# The add
def add(request):

    # We're collecting the values, from the user who posted the request
    
    value1 = int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    answer = value1 + value2

    return render(request, 'result.html', {'answer':answer})

