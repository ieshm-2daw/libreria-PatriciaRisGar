from django.urls import path
from biblioteca.views import ControlPanel, ListBooks, DetailBook, EditBook, DeleteBook,CreateBook,CreateLoan, LoanBooks, MyLoans, Newness, ReturnBook


urlpatterns = [
    path('',ListBooks.as_view(),name='listBooks'),
    path('loanBooks',LoanBooks.as_view(),name='loanBooks'),
    path('myLoans',MyLoans.as_view(),name='myLoans'),
    path('newness',Newness.as_view(),name='newness'),
    path('controlPanel',ControlPanel.as_view(),name='controlPanel'),
    path('detailBook/<int:pk>', DetailBook.as_view(), name='detailBook'),
    path('editBook/<int:pk>',EditBook.as_view(), name='editBook'),
    path('deleteBook/<int:pk>',DeleteBook.as_view(), name='deleteBook'),
    path('createBook' , CreateBook.as_view(), name='createBook'),
    path('createLoan/<int:pk>', CreateLoan.as_view(), name='createLoan'),
    path('returnBook/<int:pk>', ReturnBook.as_view(), name='returnBook'),
]