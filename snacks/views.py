from django.shortcuts import render, redirect

import snacks
from .models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializer import SnackSerializer


# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snack_list'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('list_view')


class SnacksApiList(generics.ListAPIView):
    serializer_class = SnackSerializer
    queryset = Snack.objects.all()


class SnackDetail(generics.RetrieveAPIView):
    serializer_class = SnackSerializer
    queryset = Snack.objects.all()
