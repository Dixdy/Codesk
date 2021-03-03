from django.urls import path

from .views import notelist


urlpatterns = [
    path('notelist/', notelist , name='notelist'),
]