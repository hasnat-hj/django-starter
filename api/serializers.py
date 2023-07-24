from rest_framework import serializers
from .models import Person,Author,Book

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'  # You can also specify the fields explicitly instead of '__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # You can also specify the fields explicitly instead of '__all__'
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        depth = 1
        fields = '__all__'  # You can also specify the fields explicitly instead of '__all__'
