from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"  # name of info which will be passed to html
    ordering = ["-date", "author"]  # add all order commands here

    # adjusting querying logic
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostListView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]  # add all order commands here
    context_object_name = "all_posts"

    # adjusting querying logic
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.all()
        return data


class SinglePostView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context
