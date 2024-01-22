import pytest
from django.urls import reverse
from django.http import Http404
from book_outlet.models import Book

@pytest.fixture
def create_books(db):
    books = [
        Book.objects.create(title="Test Book 1", rating=4, author="Author 1"),
        Book.objects.create(title="Test Book 2", rating=5, author="Author 2")
    ]
    return books

@pytest.mark.django_db
def test_index_view(client):
    url = reverse("index") 
    response = client.get(url)

    assert response.status_code == 200
    assert "book_outlet/index.html" in [t.name for t in response.templates]
    assert "books" in response.context
    assert "total_number_of_books" in response.context
    assert "average_rating" in response.context

@pytest.mark.django_db
def test_book_detail_view(client, create_books):
    book = create_books[0] 

    url = reverse("book-detail", args=[book.slug]) 

    response = client.get(url)
    assert response.status_code == 200
    assert "book_outlet/book_detail.html" in [t.name for t in response.templates]
    assert response.context["title"] == book.title
    assert response.context["author"] == book.author

    # Test with invalid slug
    response = client.get(reverse("book-detail", args=["non-existent-slug"]))
    assert response.status_code == 404
