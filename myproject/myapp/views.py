from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'name': 'bhanu', 'area': 'kadapa'}
    return render(request, 'home.html')
