from django.urls import path

from .views import logout_request, userLogin, registerUser


urlpatterns = [
    path('signup/', registerUser, name='signup'),
    path('logout/', logout_request, name='logout'),
    path('login/', userLogin, name='userLogin'),
]