from django.urls import path
from uploader import views

urlpatterns = [
    path('uploadquestion/',views.uploadquestion,name="uploadquestion"),
    path('uploadnotes/',views.upload_multiple_files,name="uploadnotes"),
]