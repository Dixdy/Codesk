from django.shortcuts import render

# Create your views here.

def Profile(request):
    if request.method == "POST":
        print(request.POST)
        if 'searchword' in request.POST:
            print(request.POST.get('search'))
            context = {'word' : request.POST.get('search')}
            print(context)
            return render(request, 'home.html', context)
        context = {'text' : "Your profile has been edited!"}
        return render(request, 'profile.html', context)
    return render(request, 'profile.html')