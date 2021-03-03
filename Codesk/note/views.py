from django.shortcuts import render

# Create your views here.
def notelist(request):
    ida = [1,2,3,4,5]
    title = ['test','test','test','test','test']
    tag = ['a', 'b', 'c', 'd', 'e']
    author = ['x', 'y', 'z', 's', 's']

    data = [ida, title, tag, author]
    context = { 'values': data}
    return render(request, 'notes/notelist.html',  context)

def note(request):  
    
    return render(request, 'notes/note.html')