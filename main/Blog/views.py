from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from main.Blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', "body")
    success_url = reverse_lazy('Blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', "body")
    success_url = reverse_lazy('Blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("Blog:list")