from django.contrib import admin

# Register your models here.
from .models import Person,Book,Author,Teacher

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Author)
admin.site.register(Book)