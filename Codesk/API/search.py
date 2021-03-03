from django.shortcuts import render
from django import forms
from API.database import *

def searchbar(request):
    searchkeyword = request.POST.get('search')
    print(searchkeyword)
    questionlist = searchQuestion(searchkeyword)
    print(questionlist)
    context = {'searchword':searchkeyword, 'question': questionlist}
    print(context)
    return context