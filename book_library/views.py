from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request,'book_library/index.html',context)