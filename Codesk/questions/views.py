from django.shortcuts import render
from API import search, upload

# Create your views here.
def questionlist(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)   
 
    context = search.allqns(request)
    return render(request, 'questions/questionlist.html',  context)

def questionthread(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)

        if 'submitQnComment' in request.POST:
            idx = request.POST.get('submitQnComment')
            upload.submitQnComment(request)
            context = search.qnthread(request, idx)
            return render(request, 'questions/thread.html', context)

        if 'submitAnsComment' in request.POST:
            qnansid = request.POST.get('submitAnsComment')
            ids = qnansid.split(',')
            print(ids)
            upload.submitAnsComment(request)
            context = search.qnthread(request, ids[0])
            return render(request, 'questions/thread.html',context)
            
        if 'addAnswer' in request.POST:
            idx = request.POST.get('addAnswer')
            upload.submitAnswer(request)
            context = search.qnthread(request, idx)
            return render(request, 'questions/thread.html',context)

    if request.method == "GET":
        if 'id' in request.GET:
            idx = request.GET.get("id")
            context = search.qnthread(request, idx)
            return render(request, 'questions/thread.html', context)
