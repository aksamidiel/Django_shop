from django.shortcuts import render, get_object_or_404
from .models import Book
from Catalog.models import Genre

# Create your views here.


def BookList(request, genre_name=None):
    genre=None
    genres=Genre.objects.all()
    books=Book.objects.filter(avaible=True)

    if genre_name:
        genre = get_object_or_404(Genre, name=genre_name)
        books = books.filter(genre=genre)
    return render(request, 'books/book/list.html', {
        'genre': genre,
        'genres': genres,
        'books': books
    })
# Страница товара
def BookDetail(request, id, ):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product}) 

