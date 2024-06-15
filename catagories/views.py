from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
# Create your views here.

def add_catagories(request):
    if request.method == 'POST':
        catagories_form = forms.addcatagories(request.POST)
        if catagories_form.is_valid():
            catagories_form.save()
            return redirect('add_author')
    else:
        catagories_form = forms.addcatagories(request.POST)
    return render(request, 'add_catagories.html',{'form':catagories_form})