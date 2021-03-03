from django.contrib.auth.models import User as u
from accounts.models import Question as q, QuestionComment as qc, Answer as a, AnswerComment as ac, Notes as n
from django.db.models import Q
from functools import reduce 

#Add a question into database using coursecode, title, content, author input
#author can be passed using request.user
def addQuestion(cc, tle, cnt, aut):
    newQuestion = q(coursecode=cc, title=tle, content=cnt, author=aut)
    newQuestion.save()

#Search for a list of question using user's input
def searchQuestion(input):
    keywords = input.split()
    queries = [Q(content__icontains=i) | Q(title__icontains=i) | Q(coursecode__icontains=i) for i in keywords]
    query = reduce(lambda x, y: x & y, queries)
    return q.objects.filter(query)
    #return a list of Question objects

#Search for the comment of the question
#idx refer to the index of the question
def searchQuestionComment(idx):
    return qc.objects.filter(belongs_to=q.objects.get(id=idx))
    #return a list of QuestionComment objects

#Add an answer to a question using content, belongs_to and author
#belongs_to refer to the content of the question
def addAnswer(cnt, qn, aut):
    newAnswer = a(content=cnt, belongs_to=q.objects.get(content=qn), author=aut)
    newAnswer.save()

#Search for the answer of the question
#idx refer to the index of the question  
def searchAnswer(idx):
    return a.objects.filter(belongs_to=q.objects.get(id=idx))
    #return a list of Answer objects

#Search for the comment of the answer
#idx refer to the index of the answer
def searchAnswerComment(idx):
    return ac.objects.filter(content=a.objects.get(id=idx))

#Adding a new notes
def addNotes(cc, tle, cnt, aut):
    newNotes = n(coursecode=cc, title=tle, content=cnt, author=aut)
    newNotes.save()

def searchNotes(input):
    keywords = input.split()
    queries = [Q(content__icontains=i) | Q(title__icontains=i) | Q(coursecode__icontains=i) for i in keywords]
    query = reduce(lambda x, y: x & y, queries)
    return n.objects.filter(query)

#idx refer to the idx of the notes used to identify the notes to upvotes
def upVotes(idx):
    a = n.objects.filter(id=idx)[0:1]
    a.votes = a.votes + 1
    a.save()

#idx refer to the index of the notes used to identify the notes to downvotes
def downVotes(idx):
    a = n.objects.filter(id=idx)[0:1]
    if a.votes>0:
        a.votes = a.votes - 1
        a.save()

def allNotes():
    return n.objects.all()

def allQuestions():
    return q.objects.all()