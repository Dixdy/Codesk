from django.urls import path

from note import views

urlpatterns = [
    path('notelist/', views.notelist , name='notelist'),
    path('note/', views.note, name='note')
]