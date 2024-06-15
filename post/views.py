from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        add_post = forms.postform(request.POST)
        if add_post.is_valid():
            add_post.save()
            return redirect('add_post')
    
    else:
        add_post = forms.postform()
    return render(request, 'add_post.html', {'form' : add_post})

def edit_post(request,id):
    test = models.post.objects.get(pk=id)
    post_from = forms.postform(instance=test)
    if request.method == 'POST':
        post_from = forms.postform(request.POST, instance=test)
        if post_from.is_valid():
            post_from.save()
            return redirect('home')

    return render(request, 'add_post.html', {'form' : post_from})

def delete_post(request,id):
    test = models.post.objects.get(pk=id)
    test.delete()
    return redirect('home')
