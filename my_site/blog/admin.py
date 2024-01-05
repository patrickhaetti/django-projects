from django.contrib import admin

from .models import Course, Instructor, Tag
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_filter = ("instructor", "tags", "date")
    list_display = ("title", "date", "instructor")
    prepopulated_fields = {"slug": ("title",)} 

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Tag)