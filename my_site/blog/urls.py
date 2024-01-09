from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("course", views.courses, name="course-page"),
    path("course/<slug:slug>", views.course_detail,
         name="course-detail-page") ,
    path("Ferienkurse", views.vacation_courses, name="vacation-course-page"),
    path("Ferienkurse/<slug:slug>", views.vacation_course_detail,
         name="vacation-course-detail-page") ,
]
