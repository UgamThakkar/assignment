from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post 
# Create your views here.

def Posts_list(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'User/post.html', context)

@login_required(login_url="/login")
def Create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('User:posts')
    else:
        form = forms.CreatePost()
    return render(request, 'User/create_post.html', {'form':form})