from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ninja, Weapon


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    ninjas = Ninja.objects.all()  # look familiar?
    return render(request, 'index.html', {'ninjas': ninjas})

def ninja_detail(request, ninja_id):
    ninja = Ninja.objects.get(id=ninja_id)
    #weapons gos here
    return render(request, 'ninjas/detail.html', {'ninja': ninja, })

class NinjaCreate(CreateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']
    
    
class NinjaUpdate(UpdateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']

class NinjaDelete(DeleteView):
    model = Ninja
    success_url = '/ninjas/'