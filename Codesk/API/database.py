from django.contrib.auth.models import User as u
from accounts.models import Question as q, QuestionComment as qc, Answer as a, AnswerComment as ac, Notes as n
from django.db.models import Q
from functools import reduce 

#Seach for all the questions in the database
#@param: NIL
#@return: A list of Question Object
def allQuestions():
    return q.objects.all()

#Search for a question in the database
#@param: idx (id of the question)
#@return: A Question object
def searchQuestionID(idx):
    return q.objects.filter(id=idx)[0:1]

#Search for a question related to the input in the database 
#@param: input (content OR title OR coursecode)
#@return: A list of Question Objects
def searchQuestion(input):
    keywords = input.split()
    queries = [Q(content__icontains=i) | Q(title__icontains=i) | Q(coursecode__icontains=i) for i in keywords]
    query = reduce(lambda x, y: x & y, queries)
    return q.objects.filter(query)

#Search for all the comments of a question in the database
#@param: idx (id of the question)
#@return: A list of QuestionComment Objects
def searchQuestionComment(idx):
    return qc.objects.filter(belongs_to=q.objects.get(id=idx))

#Search for all the answers of a question in the database
#@param: idx (id of the answer)
#@return: A list of Answer Objects
def searchAnswer(idx):
    return a.objects.filter(belongs_to=q.objects.get(id=idx))

#Search for all the comments of an answer in the database
#@param: idx (id of the answer)
#@return: A list of AnswerComment Objects
def searchAnswerComment(idx):
    return ac.objects.filter(belongs_to=a.objects.get(id=idx))

#Search for all the notes in the database
#@param: NIL
#@return: A list of Notes Object
def allNotes():
    return n.objects.all()

#Search for a notes in the database
#@param: idx (id of the notes)
#@return: A Notes object
def searchNoteID(idx):
    return n.objects.filter(id=idx)[0:1]    

#Search for a specific notes related to the input in the database
#@param: input (content OR title OR coursecode)
#@return: A list of Notes Object
def searchNotes(input):
    keywords = input.split()
    queries = [Q(content__icontains=i) | Q(title__icontains=i) | Q(coursecode__icontains=i) for i in keywords]
    query = reduce(lambda x, y: x & y, queries)
    return n.objects.filter(query)

#===========================================================================================================================================================================#

#Add a new question into the database
#@param: cc (coursecode of question), tle (title of question), cnt (content, the question), aut (author of the question)
#@return: NIL
def addQuestion(cc, tle, cnt, aut):
    newQuestion = q(coursecode=cc, title=tle, content=cnt, author=aut)
    newQuestion.save()

#Add a new answer into the database
#@param: cnt (content of the answer), qn(id of the question), aut (author of the answer)
#@return: NIL
def addAnswer(cnt, qn, aut):
    newAnswer = a(content=cnt, belongs_to=q.objects.get(id=qn), author=aut)
    newAnswer.save()

#Add a new notes into the database
#@param: cc (coursecode of notes), tle (title of notes), cnt (content of notes), aut (author of the notes)
#@return: NIL
def addNotes(cc, tle, cnt, aut):
    newNotes = n(coursecode=cc, title=tle, content=cnt, author=aut)
    newNotes.save()

#Add a new comment for a question into the database
#@param: cnt (content of the comment), qid (id of the question), aut (author of the comment)
#@return: NIL
def addQuestionComment(cnt, qid, aut):
    newQuestionComment = qc(content=cnt, belongs_to=q.objects.get(id=qid), author=aut)
    newQuestionComment.save()

#Add a new comment for an answer into the database
#@param: cnt (content of the comment), aid (id of the answer), aut (author of the answer)
#@return: NIL
def addAnswerComment(cnt, aid, aut):
    newAnswerComment = ac(content=cnt, belongs_to=a.objects.get(id=aid), author=aut)
    newAnswerComment.save()

#===========================================================================================================================================================================#

#Increase the vote count of an answer
#@param: idx (id of the answer)
#@return: NIL
def upVotes(idx):
    a = a.objects.filter(id=idx)[0:1]
    a.votes = a.votes + 1
    a.save()

#Decrease the vote count of an answer
#@param: idx (id of the answer)
#@return: NIL
def downVotes(idx):
    a = a.objects.filter(id=idx)[0:1]
    if a.votes>0:
        a.votes = a.votes - 1
        a.save()



