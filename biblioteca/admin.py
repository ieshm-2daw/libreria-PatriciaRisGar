from django.contrib import admin

from biblioteca.models import User,Book,Author,Publisher,Loan

# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Loan)