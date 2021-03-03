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

def allnotes(request):
    allnote = allNotes()
    context = {'notes': allnote}
    print(context)
    return context

def allqns(request):
    allqn = allQuestions()
    context = {'question': allqn}
    print(context)
    return context