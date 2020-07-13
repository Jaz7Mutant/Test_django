from django.urls import path

from .views import AvailableBooksView, EditBookView, CreateBookView, AllBooksView, UpdateBookStatusView


app_name = "books"

urlpatterns = [
    path('books/', AvailableBooksView.as_view()),
    path('books/all', AllBooksView.as_view()),
    path('books/create', CreateBookView.as_view()),
    path('books/<int:pk>', EditBookView.as_view()),
]