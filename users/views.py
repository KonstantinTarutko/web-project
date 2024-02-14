from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages

from users.forms import UserLoginForm, UserRegistrationForm


def login_or_reg(request):
    if request.method == 'POST':
        if 'password' in request.POST:
            return login(request)
    return registration(request)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Thanks for registering. Please login to continue.")
            return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
