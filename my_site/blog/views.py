from django.shortcuts import render, get_object_or_404

from .models import Course, VacationCourse

# Create your views here.

def starting_page(request):
    latest_courses = Course.objects.all().order_by("-date")[:3]
    # sorted_course = sorted(all_course, key=get_date)
    # latest_course = sorted_course[-3:]
    return render(request, "blog/index.html", {
        "course": latest_courses
    })

def courses(request):
    all_courses = Course.objects.all().order_by("-date")
    return render(request, "blog/all_courses.html", {
        "all_courses": all_courses
    })

def course_detail(request, slug):
    identified_course = get_object_or_404(Course, slug=slug)
    return render(request, "blog/course_detail.html", {
        "course": identified_course,
        "course_tags": identified_course.tags.all()
    })

def vacation_courses(request):
    all_courses = VacationCourse.objects.all().order_by("-date")
    return render(request, "blog/vacation_courses.html", {
        "all_courses": all_courses
    })

def vacation_course_detail(request, slug):
    identified_course = get_object_or_404(VacationCourse, slug=slug)
    return render(request, "blog/vacation_course_detail.html", {
        "course": identified_course,
        "course_tags": identified_course.tags.all()
    })
