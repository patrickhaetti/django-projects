from django.db import models
from django.core.validators import MinLengthValidator
from datetime import timedelta

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Location(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    image_name = models.CharField(max_length=100)
    
class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
         return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
     
class Course(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, related_name="courses")
    tags = models.ManyToManyField(Tag)
     
class VacationCourse(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, related_name="vacationcourses")
    tags = models.ManyToManyField(Tag)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    price_members = models.DecimalField(max_digits=10, decimal_places=2, default=55.00)
    price_nonMembers = models.DecimalField(max_digits=20, decimal_places=2, default=69.00)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, related_name="location")
