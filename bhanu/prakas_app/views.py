from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name (request):
    a,b=10, 2
    add=a+b
    return render(request, 'home.html', {'name': 'addition of two num'})
def add(request):
    val1= int(request.POST['num1'])
    val2= int(request.POST['num2'])
    result= val1+val2
    return render(request, "result.html", {'res': result})
def ok(request):
    pass

