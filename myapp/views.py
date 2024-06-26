from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import contactModel


# Create your views here.


@login_required(login_url='register')
def home(request):
    return render(request, 'home.html')



def contactPage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        city=request.POST['city']

        if contactModel.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exist')
            return redirect('home')
        else:
            data= contactModel.objects.create(name=name,email=email,contact=contact,city=city)
            data.save()
            messages.success(request, 'Successfully Your Submited !')
            return redirect('home')
    return render(request, 'contact.html')




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
            return redirect('login')

    return render(request, 'login.html')



def logoutPage(request):
    logout(request)
    messages.success(request, 'Successfull Logout !')
    return redirect('login')
