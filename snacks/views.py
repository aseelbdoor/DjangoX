from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from .models import Snack

class SnackListView(ListView):
    template_name='snacks/snackList.html'
    model=Snack

class SnackDetailView(DetailView):
    template_name='snacks/snackDetails.html'
    model=Snack

class SnackCreateView(CreateView):
    template_name = 'snacks/snackCreate.html'
    model = Snack
    fields=['title','purchaser','description']

class SnackUpdateView(UpdateView):
    template_name='snacks/snackUpdate.html'
    model=Snack
    fields='__all__'
    success_url = reverse_lazy('List')

class SnackDeleteView(DeleteView):
    template_name='snacks/snackDelete.html'
    model=Snack
    success_url = reverse_lazy('List')
