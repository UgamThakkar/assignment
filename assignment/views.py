from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("User:posts")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
   



def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('User:posts')
    else:
        form = CreateUserForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)