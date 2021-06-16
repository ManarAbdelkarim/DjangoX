from django.shortcuts import render
from django.views.generic import  ListView , DetailView , CreateView , DeleteView ,UpdateView
from .models import Anime
from django.urls import reverse_lazy
# Create your views here.

class AnimeListView(ListView):
    template_name = "anime/anime_list.html"
    model = Anime

class AnimeDetailView(DetailView):
    template_name = "anime/anime_detail.html"
    model = Anime

class AnimeCreateView(CreateView):
    template_name = "anime/anime_create.html"
    model = Anime
    fields = ['title','author', 'image','description']

class AnimeUpdateView(UpdateView):
    template_name = "anime/anime_update.html"
    model = Anime
    fields = ['title','author', 'image','description']

class AnimeDeleteView(DeleteView):
    template_name = "anime/anime_delete.html"
    model = Anime
    success_url = reverse_lazy('anime/anime_list')