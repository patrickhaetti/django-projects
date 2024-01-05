from django.shortcuts import render
from datetime import date

from .models import Post

all_posts = [
]

# create helper function
def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    print(latest_posts)
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post
    })
