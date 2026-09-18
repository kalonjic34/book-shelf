from django.urls import path
from . import views

app_name = "book_library"
urlpatterns = [
    path("", views.index, name="index")
]