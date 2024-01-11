from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from rest_framework.generics import ListAPIView

from .models import Review, ReviewSerializer
from .forms import ReviewForm

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

# use TemplateView as specific view for templates
class ThankYou(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # adjusting querying logic
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=2)
        return data

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

# RESTful API view for Review list
class ReviewListAPIView(ListAPIView):
    # queryset = Review.objects.filter(rating__gt=2)  # adjusting querying logic
    queryset = Review.objects.all()  
    serializer_class = ReviewSerializer