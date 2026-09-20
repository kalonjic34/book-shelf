from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from book_library.forms import BookForm, GenreForm
from .models import Book,Genre
from django.contrib.auth.decorators import login_required

def index(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request,'book_library/index.html',context)
@login_required
def genres(request):
    # genres = Genre.objects.all()
    genres = Genre.objects.filter(owner=request.user)
    context = {"genres":genres}
    return render(request,'book_library/genres.html',context )

@login_required
def genre(request,genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if genre.owner != request.user:
        raise Http404
    books=genre.book_set.order_by('-date_added')
    context = {"genre":genre,'books':books}
    return render(request, "book_library/genre.html",context)

@login_required
def new_genre(request):
    if request.method != 'POST':
        form=GenreForm()
    else:
        form=GenreForm(data=request.POST)
        
        if form.is_valid():
            
            new_genre = form.save(commit=False)
            new_genre.owner = request.user
            new_genre.save()
            return redirect('book_library:genres')
        
    context ={'form':form}
    return render(request, 'book_library/new_genre.html', context)

@login_required
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

@login_required
def edit_book(request,book_id):
    book = Book.objects.get(id=book_id)
    genre= book.genre
    if genre.owner != request.user:
        raise Http404
    if request.method != "POST":
        form=BookForm(instance=book)
    else:
        form=BookForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_library:genre",genre_id=genre.id)
    context={
        "book":book,
        "genre":genre,
        "form":form
    }
    return render(request, "book_library/edit_book.html",context) 
