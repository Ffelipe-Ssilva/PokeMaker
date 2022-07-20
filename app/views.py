from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import PokemonForm
from app.models import Pokemon
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data={}
    search=request.GET.get('search')
    if search:
        data['db']=Pokemon.objects.filter(name__icontains=search)
    else:
        data['db']=Pokemon.objects.all()
    #all = Pokemon.objects.all()
    #paginator = Paginator(all, 2)
    #pages=request.GET.get('page')
    #data['db']=paginator.get_page(pages)
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
    return redirect('home')