
from django.db.models import Max
from datetime import date, timedelta
from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from biblioteca.models import Book, Loan
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#listado de libros disponibles
class ListBooks (ListView):
    model = Book
    templete_name = 'biblioteca/book_list.html'
    def get_context_data(self,**kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['available_Books'] = Book.objects.filter(availability='available')
            context['loaned_Books'] = Book.objects.filter(availability='loaned')
            
            allGenres =[]
            for book in Book.objects.all():
                if book.genre not in allGenres:
                    allGenres.append(book.genre)
            context['generateFilter'] = allGenres 

            genreSelected = self.request.GET.getlist('genre')
            if genreSelected:
                context['listFiltertGenre'] = genreSelected
                for gen in genreSelected:                    
                    context['available_Books'] = context['available_Books'].filter(genre=gen)
                    context['loaned_Books'] = context['loaned_Books'].filter(genre=gen)
            
            return context

#listado de libros prestados
class LoanBooks (LoginRequiredMixin,ListView):
    model = Book
    template_name = 'biblioteca/books_loan.html'
    paginate_by = 2
    queryset = Book.objects.filter(availability = 'loaned')

#detalle de libro
class DetailBook (DetailView):
    model = Book
    template_name = 'biblioteca/book_detail.html'

#editar libro
class EditBook (LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['title','authors','publisher','rating','publicationDate','genre','isbn','sumary','availability']
    template_name = 'biblioteca/book_edit.html'
    success_url = reverse_lazy('listBooks')

#borrar libro
class DeleteBook (LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'biblioteca/delete.html'
    success_url = reverse_lazy ('listBooks')

#Añadir libro
class CreateBook (LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title','authors', 'publicationDate','publisher','rating','genre','isbn','sumary','availability','cover']
    template_name = 'biblioteca/book_create.html'
    success_url = reverse_lazy('listBooks')


#Crear prestamo
class CreateLoan(LoginRequiredMixin,View):
    templateList = 'biblioteca/loan_create.html'

    def get (self, request,pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request,self.templateList,{'book':book})

    def post (self,request,pk):

        book = get_object_or_404(Book, pk=pk)
        book.availability = 'loaned'
        book.save()

        Loan.objects.create(
                book = book,
                user = request.user,
                loanDate = date.today(),
                returnDate = date.today() + timedelta(days=30),
            )
        return redirect ('detailBook', pk=pk)

#Devolver libro
class ReturnBook(LoginRequiredMixin,View):
    templateList = 'biblioteca/book_return.html'

    def get (self,request,pk):
        bookLoaned = get_object_or_404(Book, pk=pk)
        return render(request,self.templateList,{'book':bookLoaned})

    def post (self,request,pk):
        bookLoaned = get_object_or_404(Book, pk=pk)
        loan = get_object_or_404(Loan,book=bookLoaned,user=request.user,status='loaned')

        loan.status = 'returned'
        loan.returnDate = date.today()
        loan.save()

        bookLoaned.availability = 'available'
        bookLoaned.save()

        return redirect('detailBook', pk=pk)
    
# Listado de mis prestamos diferenciando devuletos y prestados
class MyLoans(LoginRequiredMixin,ListView):
        model = Loan
        template_name = 'biblioteca/loan_list.html'

        def get_context_data(self,**kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['loaned_Loans'] = Loan.objects.filter(status='loaned', user = self.request.user)
            context['returned_Loans'] = Loan.objects.filter(status='returned', user = self.request.user)

            return context

#Listar libros nuevosbook
class Newness (ListView):
    model = Book
    template_name = 'biblioteca/book_newness.html'

    queryset = Book.objects.filter(publicationDate__gt=date.today() - timedelta(days=30)) 

#Panel de control bibliotecario
class ControlPanel (LoginRequiredMixin,ListView):
    model = Loan
    template_name = 'biblioteca/panel.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['loanCount'] = Loan.objects.count()
        context['availableBooks'] = Book.objects.filter(availability = 'available').count()
        context['noReturned'] = Loan.objects.filter(returnDate__lt=date.today(), status = 'loaned')
        context['upcomingLoans'] = Loan.objects.filter(returnDate__lt= date.today() + timedelta(days=7), status = 'loaned')
        context['topRatingBook'] = Book.objects.all().order_by('-rating')
        
        return context
