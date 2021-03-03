from django.urls import path

from questions import views

urlpatterns = [
    path('questionlist/', views.questionlist , name='questionlist'),
    path('thread/', views.questionthread, name='thread'),
]