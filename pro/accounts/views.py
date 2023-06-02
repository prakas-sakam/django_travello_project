from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm password']
        if password1 == password2:
            if user.objects.filter(username=username).exist():
                messages.info(request,'user name taken')
                return redirect('register')
            elif user.objects.filter(email=email).exist():
                messages.info(request,'email is exist')
                return redirect('register')
            else:
                user=user.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)  
                user.save();
                print('user created..')
        else:
            messages.info('request,password naot match')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')


# Create your views here.
