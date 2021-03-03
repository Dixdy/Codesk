from django.shortcuts import render
from django import forms

# Create your views here.

def Profile(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            searchkeyword = request.POST.get('search')
            print(searchkeyword)
            #context = databasefunction(searchkeyword)
            context = {'word':searchkeyword}
            print(context)
            return render(request, 'home.html', context)
        context = {'text' : "Your profile has been edited!"}
        return render(request, 'profile.html', context)
    return render(request, 'profile.html')