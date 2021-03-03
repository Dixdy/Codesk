from django.shortcuts import render
from django import forms
from API.database import *

# Create your views here.

def Profile(request):
    print(searchQuestion('Tutorial'))
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)
        context = {'text' : "Your profile has been edited!"}
        return render(request, 'profile.html', context)
    return render(request, 'profile.html')