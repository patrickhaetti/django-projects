from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
