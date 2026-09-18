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