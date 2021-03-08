from django.shortcuts import render
from django import forms
from API import search

def Home(request):
    if request.method == "POST":
        context = search.searchbar(request)
        return render(request, 'results.html', context)
    return render(request, 'home.html')