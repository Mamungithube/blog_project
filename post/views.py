from django.shortcuts import render, redirect
from . import forms
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