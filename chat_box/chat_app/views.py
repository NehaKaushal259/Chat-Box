from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request , "home.html")




def loginpage(request):

    if request.method == "POST":
        username = request.POST.get("username",'')
        email = request.POST.get("email",'')
        password = request.POST.get("password",'')
        user = authenticate(request , username = username , email = email , password = password)

        if user is not None:
            login(request , user)
            return redirect('home')
        
        else:
            return redirect('login')


    return render(request, 'login.html')




def logoutUser(request):
    logout(request)
    return redirect('home')





def register(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        email = request.POST.get("email", '')
        password1 = request.POST.get("password1", '')
        password2 = request.POST.get("password2", '')

        # print(username, email, password1, password2)

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')





# Neha111@ // Neha
# 123456 // Anchal
# 09870987 // kalash