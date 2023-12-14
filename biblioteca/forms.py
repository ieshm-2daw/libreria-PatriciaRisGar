
from django import forms

from biblioteca.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title','authors','publisher','rating', 'publicationDate', 'genre','isbn','sumary','availability','cover'
        ]