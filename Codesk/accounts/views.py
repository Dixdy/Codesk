from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_request(request):
    username = request.user
    messages.info(request, f"{username}, you have successfully logged out!")
    logout(request)
    return redirect('home')