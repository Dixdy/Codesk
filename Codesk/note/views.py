from django.shortcuts import render
from API import search

# Create your views here.
def notelist(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)   
 
    context = search.allnotes(request)
    return render(request, 'notes/notelist.html',  context)


def note(request):  
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)   
            
    return render(request, 'notes/note.html')