from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "image_1.png",
        "author": "Test",
        "date": "2023-10-07",
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views when you get when hiking in the mountains!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima unde, vitae deserunt et provident officia commodi neque voluptatem eligendi dolores reiciendis delectus! Voluptatibus maxime quis quisquam, nisi ullam velit exercitationem."
    },
    {
        "slug": "forest-adventure",
        "image": "image_2.png",
        "author": "Explorer",
        "date": "2023-10-08",
        "title": "Journey Through the Forest",
        "excerpt": "Exploring the deep forests offers a unique perspective of nature.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, quod. Ratione, voluptatum. Velit, minus. Necessitatibus, eius."
    },
    {
        "slug": "beach-sunset",
        "image": "image_3.png",
        "author": "Beachlover",
        "date": "2023-10-09",
        "title": "Sunset at the Beach",
        "excerpt": "Watching the sunset over the ocean is a mesmerizing experience.",
        "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam, quidem."
    },
    {
        "slug": "city-exploration",
        "image": "image_4.png",
        "author": "UrbanWalker",
        "date": "2023-10-10",
        "title": "Exploring the City",
        "excerpt": "The hustle and bustle of the city have their own charm.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, sapiente!"
    },
    {
        "slug": "desert-mystique",
        "image": "image_5.png",
        "author": "DesertFan",
        "date": "2023-10-11",
        "title": "Mysteries of the Desert",
        "excerpt": "The desert landscapes hold many secrets waiting to be discovered.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti, magni."
    },
    {
        "slug": "snowy-peaks",
        "image": "image_6.png",
        "author": "MountainClimber",
        "date": "2023-10-12",
        "title": "Climbing the Snowy Peaks",
        "excerpt": "The challenge of climbing snowy mountains is both thrilling and rewarding.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, obcaecati."
    }
]

# create helper function
def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all_posts.html")

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")
