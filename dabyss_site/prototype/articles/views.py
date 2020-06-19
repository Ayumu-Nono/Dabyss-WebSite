from django.shortcuts import render
from .models import BlogArticle, HomeArticle, GamesArticle
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    template_name = "blog/listview.html"
    model = BlogArticle
    pagenate_by = 10
