from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # not possible when prepopulated_fields
    prepopulated_fields = {"slug": ("title",)}  # editable=False not possible in Book model then

admin.site.register(Book, BookAdmin)