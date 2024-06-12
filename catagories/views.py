from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
# Create your views here.

def add_catagories(request):
    if request.method == 'POST':
        author_form = forms.addcatagories(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = forms.addcatagories(request.POST)
    return render(request, 'add_author.html',{'form':author_form})