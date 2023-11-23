from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):

    dni = models.CharField(max_length=9)
    address = models.CharField(max_length=30)
    phoneNumber = models.IntegerField()

class Book(models.Model):
    STATUS = [('available', 'Available'),('loaned', 'Loaned'), ('loanProcess','In loan process'),]

    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    publisher =  models.ForeignKey('Publisher',on_delete=models.CASCADE)
    publicationDate = models.DateField()
    genre = models.CharField(max_length=10)
    isbn = models.CharField(max_length=10, unique = True)
    sumary = models.TextField()
    availability = models.CharField(max_length=11,choices=STATUS, default='available')
    cover = models.ImageField()


class Author(models.Model):
    name = models.CharField(max_length=30)
    biograohy = models.TextField()
    photo = models.ImageField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website = models.URLField()


class Loan (models.Model):
    STATUS = [('loaned', 'Loaned'), ('returned','Returned')]

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    loanDate = models.DateField()
    returnDate = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=11,choices=STATUS, default='loaned')

