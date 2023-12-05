from django.urls import path
from biblioteca.views import ListBooks, DetailBook, EditBook, DeleteBook,CreateBook,CreateLoan


urlpatterns = [
    path('',ListBooks.as_view(),name='listBooks'),
    path('detailBook/<int:pk>', DetailBook.as_view(), name='detailBook'),
    path('editBook/<int:pk>',EditBook.as_view(), name='editBook'),
    path('deleteBook/<int:pk>',DeleteBook.as_view(), name='deleteBook'),
    path('createBook' , CreateBook.as_view(), name='createBook'),
    path('createLoan/<int:pk>', CreateLoan.as_view(), name='createLoan'),
]