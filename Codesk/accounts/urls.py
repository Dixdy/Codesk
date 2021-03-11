from django.urls import path

from .views import SignUpView, logout_request, userLogin


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_request, name='logout'),
    path('login/', userLogin, name='login'),
]