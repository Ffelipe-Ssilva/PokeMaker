from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import PokemonForm

# Create your views here.
def home(request):
    data={}
    data['pokemon']='Rildfglaboom'
    return render(request,'index.html',data)


def form(request):
    data={}
    data['form']=PokemonForm()
    return render(request,'formulario.html',data)


def create(request):
    form = PokemonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')