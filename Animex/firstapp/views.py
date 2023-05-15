from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def car(request):
    return render(request,'carousel.html')

def moive(request):
    if request.user.username == '':
         return redirect('signin')
        
    return render(request,'moive.html')



def ch(request):
    return render(request,'index.html')

# def home(request):
#     if request.user.username == '':
#         return redirect('signin')
#     return render(request, 'home.html')


def signin(request):
    if request.user.username == '':
        if request.POST:
            username_val = request.POST.get('username')
            password_val = request.POST.get('password')
            user = authenticate(username=username_val, password=password_val)
            if user is not None:
                login(request=request, user=user)
                messages.success(request, 'signin successful!')
                return redirect('moive')
            messages.error(request, "invalid username or password")
        return render(request, 'signin.html')
    else:
        return redirect('moive')

def signout(request):
    if request.user.username != '':
        logout(request)
    return redirect('signin')

def registration(request):
    if request.user.username == '':
        if request.POST:
            username_val = request.POST.get('username')
            email_val = request.POST.get('email')
            firstname_val = request.POST.get('firstname')
            lasrname_val = request.POST.get('lastname')
            password_val = request.POST.get('password')

            try:
                user = User.objects.create_user(
                    username=username_val,
                    email=email_val,
                    first_name=firstname_val,
                    last_name=lasrname_val,
                    password=password_val)
                messages.success(request, 'your account has been created successfully')

            except:
            
                messages.error(request, 'Error occured! not able to create account.')
        return render(request, 'register.html')
    else:
        return redirect('moive')
    


