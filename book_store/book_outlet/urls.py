from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.book_detail, name="book-detail") # make sure id is int
]
