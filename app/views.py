from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import PokemonForm
from app.models import Pokemon

# Create your views here.
def home(request):
    data={}
    data['db']=Pokemon.objects.all()
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

def view(request, pk):
    data={}
    data['db']=Pokemon.objects.get(pk=pk)
    return render(request,'view.html', data)

def edit(request, pk):
    data={}
    data['db']=Pokemon.objects.get(pk=pk)
    data['form']=PokemonForm(instance=data['db'])
    return render(request,'formulario.html', data)

def update(request, pk):
    data={}
    data['db']=Pokemon.objects.get(pk=pk)
    form=PokemonForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db=Pokemon.objects.get(pk=pk)
    db.delete()
    return render(request,'index.html')