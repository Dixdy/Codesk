from django.shortcuts import render, redirect
from uploader.forms import ImageFileForm
from uploader.models import ImageFile
import pytesseract

def uploadquestion(request):
    data = dict()
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    image_form = ImageFileForm(request.POST or None, request.FILES or None)
    print(image_form.is_valid())
    if image_form.is_valid():
        image = image_form.save()
        image.execute_and_save_ocr()
        redirect('home')
    image_last = ImageFile.objects.last()
    image_list = ImageFile.objects.all().order_by('-id')

    data['image_form'] = image_form
    data['image_list'] = image_list
    data['image_last'] = image_last
    return render(request, "uploader/index.html", data)
