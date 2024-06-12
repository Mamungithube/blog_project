from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
# Create your views here.

def profiles_form(request):
    if request.method == 'POST':
        profiles_form = forms.profiles_form(request.POST)
        if profiles_form.is_valid():
            profiles_form.save()
            return redirect('add_profile')
    else:
        profiles_form = forms.profiles_form(request.POST)
    return render(request, 'add_profile.html',{'form':profiles_form})