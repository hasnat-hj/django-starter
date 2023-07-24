from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    # Add more fields as needed
    # e.g., address, phone, etc.

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more fields as needed
    # e.g., address, phone, etc.

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)