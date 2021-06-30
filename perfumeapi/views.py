from django.shortcuts import render, redirect
from perfumeapi.forms import PerfumesForm
from perfumeapi.models import Perfumes


# Create your views here.
def home(request):
    data = {}
    data['db'] = Perfumes.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = PerfumesForm()
    return render(request, 'form.html', data)

def create(request):
    form = PerfumesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Perfumes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Perfumes.objects.get(pk=pk)
    data['form'] = PerfumesForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Perfumes.objects.get(pk=pk)
    form = PerfumesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(pk):
    db = Perfumes.objects.get(pk=pk)
    db.delete()
    return redirect('home')
