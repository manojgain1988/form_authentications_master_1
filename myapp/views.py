from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


# @login_required(login_url='register')
def home(request):
    return render(request, 'home.html')



def registerPage(request):
    if request.method == "POST":
        ful_name = request.POST.get('ful_name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, 'Your Password and Confirm Passwor are not Same !')
            return redirect('register')
            # return HttpResponse('Your Password and Confirm Passwor are not Same')

        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, 'Your Register Successfull !')
            return redirect('login')

    return render(request, 'register.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request, username=username,password=pass1)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfull Your Logined !')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is Invalid !')
            # return HttpResponse ('Username or Password is Incorrect')
            return redirect('home')

    return render(request, 'login.html')





def logoutPage(request):
    logout(request)
    messages.success(request, 'Successfull Your Deleted !')
    return redirect('login')
