from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class User(AbstractUser):

    dni = models.CharField(max_length=9)
    address = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=11)

    def __str__(self):
        return self.username

class Book(models.Model):
    STATUS = [('available', 'Available'),('loaned', 'Loaned'), ('loanProcess','In loan process'),]

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author')
    publisher =  models.ForeignKey('Publisher',on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    publicationDate = models.DateField()
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    sumary = models.TextField()
    availability = models.CharField(max_length=11,choices=STATUS, default='available')
    cover = models.ImageField(upload_to='cover', null = True, blank = True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    biograohy = models.TextField()
    photo = models.ImageField(upload_to='photo',null = True, blank = True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class Loan (models.Model):
    STATUS = [('loaned', 'Loaned'), ('returned','Returned')]

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    loanDate = models.DateField()
    returnDate = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=11,choices=STATUS, default='loaned')

    def __str__(self):
        return f'Prestamo de {self.book.title} a {self.user}'
