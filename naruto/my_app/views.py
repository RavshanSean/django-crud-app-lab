from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ninja, Weapon



class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def index(request):
    ninjas = Ninja.objects.filter(user=request.user)# look familiar?
    return render(request, 'index.html', {'ninjas': ninjas})

def ninja_detail(request, ninja_id):
    ninja = Ninja.objects.get(id=ninja_id)
    #weapons gos here
    return render(request, 'ninjas/detail.html', {'ninja': ninja, })

class NinjaCreate(LoginRequiredMixin, CreateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class NinjaUpdate(LoginRequiredMixin, UpdateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']

class NinjaDelete(LoginRequiredMixin, DeleteView):
    model = Ninja
    success_url = '/ninjas/'
    

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
    