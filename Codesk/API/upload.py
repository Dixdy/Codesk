from django.shortcuts import render
from django import forms
from API.database import *


def submitQnComment(request):
    idx = request.POST.get('submitQnComment')
    print(idx)
    cnt = request.POST.get('qncomment')
    print(cnt)
    addQuestionComment(cnt, idx, request.user)


def submitAnsComment(request):
    qnansid = request.POST.get('submitAnsComment')
    ids = qnansid.split(',')
    print(ids)
    cnt = request.POST.get('anstext'+ids[1])
    print(cnt)
    addAnswerComment(cnt, int(ids[1]), request.user)


def submitAnswer(request):
    idx = request.POST.get('addAnswer')
    cnt = request.POST.get('AnsText')
    print(cnt)
    addAnswer(cnt, idx, request.user)


def uploadQn(request):
    cc = "test"
    tle = request.POST.get('titletxt')
    cnt = request.POST.get('txtbx')
    print(cnt)
    addQuestion(cc, tle, cnt, request.user)
