from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from API import search
from django.contrib.auth.forms import UserCreationForm

def registerUser(request):
    if request.method == 'POST':
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_request(request):
    username = request.user
    messages.success(request, f"{username}, you have successfully logged out!")
    logout(request)
    return redirect('home')

def userLogin(request):
    context = {}
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'msg':'Failed'}
    return render(request, 'registration/login.html', context)

