from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm

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


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm(),
          "comments": post.comments.all().order_by("-id")

        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()

          return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form,
          "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post_detail.html", context)
    
class ReadLaterView(View):
    def post(self, request):
        pass