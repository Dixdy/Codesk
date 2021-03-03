from django.shortcuts import render

# Create your views here.
def questionlist(request):
    ida = [1,2,3,4,5]
    title = ['testq','testq2','testq3','testq4','testq5']
    tag = ['a', 'b', 'c', 'd', 'e']
    author = ['x', 'y', 'z', 's', 's']
    commentsc = [4,5,7,8,20]
    context = {"id": ida, 'title': title, 'tag': tag, 'author': author, 'comment': commentsc}
    return render(request, 'questions/questionlist.html',  context)

def questionthread(request):
    
    return render(request, 'questions/thread.html')
