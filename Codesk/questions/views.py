from django.shortcuts import render
from API import search

# Create your views here.
def questionlist(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)   
 
    context = search.allqns(request)
    return render(request, 'questions/questionlist.html',  context)

def questionthread(request):
    
    return render(request, 'questions/thread.html')
