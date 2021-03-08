from django.shortcuts import render
from django import forms
from API.database import *

def searchbar(request):
    searchkeyword = request.POST.get('search')
    questionlist = searchQuestion(searchkeyword)
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

def qnthread(request, idx):
    context = {}
    ansclist = []
    qn = searchQuestionID(idx)
    context['question'] = qn
    qncomment = searchQuestionComment(idx)
    context['qnComments'] = qncomment
    ans = searchAnswer(idx)
    context['answer'] = ans
    for i in ans.values('id'):
        idlist = list(i.values())
        print(idlist)
        for x in idlist:
            cmt = searchAnswerComment(x)
            ansclist.append(cmt)
            print(searchAnswerComment(x))
    context["comments"] = ansclist
    print(ansclist)

    return context

