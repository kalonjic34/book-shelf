from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book,Genre

def index(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request,'book_library/index.html',context)

def genres(request):
    genres = Genre.objects.all()
    context = {"genres":genres}
    return render(request,'book_library/genres.html',context )

def genre(request,genre_id):
    genre = Genre.objects.get(pk=genre_id)
    books=genre.book_set.order_by('-date_added')
    context = {"genre":genre,'books':books}
    return render(request, "book_library/genre.html",context)