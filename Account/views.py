from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'Accounts/home.html')


def login_page(request):
    if request.method == 'post':
        name = request.post['name']

        password = request.post['password']
        user = authenticate(username=name, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are Logged In")
            return redirect('home')
        else:
            messages.error(request, 'Your Username or Password is Incorrect')
            return redirect('home')

        return redirect('home')

    return render(request, 'Accounts/login.html')


def registration_page(request):
    if request.method == 'post':
        name = request.post['name']
        email = request.post['email']
        password = request.post['password']
        password1 = request.post['password1']
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'username Already Exists , Choose Another one')
                return redirect('reg')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.set_password(password)
                messages.success(request, 'Log In Success')
                user.save()
            return redirect('login')
        else:
            messages.error(request, 'Please Make Password Same')
            return redirect('reg')

    return render(request, 'Accounts/registration.html')


def log_out(request):
    logout(request)
    messages.success(request, 'Log out Success')
    return redirect('login')


def forget_pass(request):
    if request.method == 'post':
        name = request.post['name']
        email = request.post['email']
        password = request.post['password']
        use = User.object.get(username=name)
        if User.email == email:
            User.set_password(password)
            update_session_auth_hash(request, use)
            messages.succes(request, 'password change done')
            return redirect('login')
        else:
            messages.error(request, 'email not matched')
    return render(request, 'Account/forget_pass.html')


@login_required(login_url='login')
def prof_page(request):
    return render(request, 'Accounts/profile.html')
