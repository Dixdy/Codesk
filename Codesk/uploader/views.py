from django.shortcuts import render, redirect
from uploader.forms import ImageFileForm, UploadFileForm
from uploader.models import ImageFile
import pytesseract
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from API import search

def uploadquestion(request):
    if request.method == "POST":
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)   


    data = dict()
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    image_form = ImageFileForm(request.POST or None, request.FILES or None)
    print(image_form.is_valid())

    if ImageFile.objects.count() > 0:
        ImageFile.objects.all().delete()

    if image_form.is_valid():
        image = image_form.save()
        image.execute_and_save_ocr()
        redirect('uploadquestion')
    image_last = ImageFile.objects.last()
    image_list = ImageFile.objects.all().order_by('-id')

    data['image_form'] = image_form
    data['image_list'] = image_list
    data['image_last'] = image_last
    return render(request, "uploader/index.html", data)

@ensure_csrf_cookie
def upload_multiple_files(request):
    if request.method == 'POST':
        if 'searchword' in request.POST:
            context = search.searchbar(request)
            return render(request, 'results.html', context)
        else:   
            form = UploadFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('files')
            if form.is_valid():
                for f in files:
                    handle_uploaded_file(f)
                context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
                return render(request, "uploader/multiple.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'uploader/multiple.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)