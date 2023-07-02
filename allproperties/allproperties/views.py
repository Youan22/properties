from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post


def index(request):
    return render(request, 'allproperties/index.html')

def allproperties(request):
    # Your implementation here
    pass

def buy(request):
    # Your implementation here
    pass

def rent(request):
    # Your implementation here
    pass

def contactus(request):
    # Your implementation here
    pass
