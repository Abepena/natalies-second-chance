from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Dog
from .forms import DogCreateForm


class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogCreateForm


class DogListView(ListView):
    model = Dog
    template_name = "dogs/dog_list.html"
    context_object_name = 'dogs'
    paginate_by = 10


class DogDetailView(DetailView):
    form_class = DogCreateForm
    model = Dog
    template_name = 'dogs/dog_detail.html'


class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogCreateForm
    template_name = "dogs/dog_form.html"


class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:list')
    context_object_name = 'dog'