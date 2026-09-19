from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from book_library.forms import BookForm, GenreForm
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
def new_genre(request):
    if request.method != 'POST':
        form=GenreForm()
    else:
        form=GenreForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('book_library:genres')
        
    context ={'form':form}
    return render(request, 'book_library/new_genre.html', context)

def new_book(request,genre_id):
    genre = Genre.objects.get(id=genre_id)
    if request.method != 'POST':
        form=BookForm()
    else:
        form= BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.genre=genre
            new_book.save()
            return redirect("book_library:genre", genre_id=genre.id)
    context={
        "genre":genre,
        "form":form
    }
    return render(request, "book_library/new_book.html",context)
