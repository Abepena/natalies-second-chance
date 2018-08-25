from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog
from .forms import DogCreateForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class EventPageView(TemplateView):
    template_name = 'events.html'

class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogCreateForm
    template_name = "pets/dog_create.html"

class DogListView(ListView):
    model = Dog
    template_name = "pets/dog_list.html"

class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    template_name = "TEMPLATE_NAME"

class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    template_name = "pets/dog_delete.html"

