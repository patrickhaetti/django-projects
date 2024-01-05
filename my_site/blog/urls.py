from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("course", views.courses, name="course-page"),
    path("course/<slug:slug>", views.course_detail,
         name="course-detail-page") 
]
