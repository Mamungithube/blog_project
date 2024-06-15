from django.shortcuts import render
from post.models import post
# Create your views here.

def home(request):
    data = post.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})