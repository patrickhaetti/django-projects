import pytest
from django.urls import reverse
from django.core.exceptions import ValidationError
from book_outlet.models import Book

@pytest.mark.django_db
def test_book_creation():
    book = Book.objects.create(
        title="Test Book",
        rating=4,
        author="John Doe"
    )
    assert book.title == "Test Book"
    assert book.rating == 4
    assert book.author == "John Doe"
    assert book.is_bestselling == False

@pytest.mark.django_db
def test_book_creation_failure():
    # Test with a title that is too long
    long_title = "x" * 51  # 51 characters long
    with pytest.raises(ValidationError):
        Book.objects.create(
            title=long_title,
            rating=4,
            author="John Doe"
        ).full_clean()  # Call full_clean to trigger the validation

    # Test with a rating that is too high
    with pytest.raises(ValidationError):
        Book.objects.create(
            title="Valid Title",
            rating=6,  # Rating higher than the maximum allowed
            author="Jane Doe"
        ).full_clean()  # Call full_clean to trigger the validation


@pytest.mark.django_db
def test_slug_generation():
    book = Book.objects.create(
        title="Test Book with Slug",
        rating=3,
        author="Jane Doe"
    )
    assert book.slug == "test-book-with-slug"

@pytest.mark.django_db
def test_get_absolute_url():
    book = Book.objects.create(
        title="Another Test Book",
        rating=5,
        author="Author Name"
    )
    url = reverse("book-detail", args=[book.slug])
    assert book.get_absolute_url() == url

@pytest.mark.django_db
def test_book_str_representation():
    book = Book.objects.create(
        title="My Test Book",
        rating=2,
        author="Author Test"
    )
    assert str(book) == "My Test Book >> rating: 2"
