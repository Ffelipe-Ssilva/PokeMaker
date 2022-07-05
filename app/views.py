from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data={}
    data['pokemon']='Rillaboom'
    return render(request,'index.html',data)


def form(request):
    return render(request,'formulario.html')