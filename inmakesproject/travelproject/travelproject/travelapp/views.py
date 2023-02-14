from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Teammates
# Create your views here.
def fun1(request):
    x=Place.objects.all()
    y=Teammates.objects.all()
    return render(request,"index.html",{"key":x,"key1":y})

    