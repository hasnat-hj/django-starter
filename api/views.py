from rest_framework import generics
from .models import Person,Teacher,Author,Book
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer,BookSerializer,AuthorSerializer
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from django.forms import model_to_dict
import json

# django apis from scratch
class TeacherListView(View):
    def get(self, request, teacher_id=None):
        if teacher_id is not None:
            try:
                teacher = Teacher.objects.get(pk=teacher_id)
                teacher_data = {
                    "id": teacher.id,
                    "name": teacher.name,
                    "age": teacher.age
                }
                return JsonResponse(teacher_data, status=200)
            except Teacher.DoesNotExist:
                return JsonResponse({'error': 'Teacher not found.'}, status=404)
        else:
            teachers = Teacher.objects.all()
            data = [{'id': teacher.id, 'name': teacher.name, 'age': teacher.age} for teacher in teachers]
            return JsonResponse(data, safe=False, status=200)

    def post(self, request):
            try:
                data = json.loads(request.body)
                name = data.get('name')
                age = data.get('age')
                if name and age:
                    teacher = Teacher(name=name, age=age)
                    teacher.save()
                    # for queryset
                    # data = serializers.serialize('json',teacher)
                    data =  model_to_dict(teacher)
                    return JsonResponse(data, status=201)
                else:
                    return JsonResponse({'error': 'Name and age are required fields.'}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

   
    def put(self, request, teacher_id):
        teacher = Teacher.objects.get(pk=teacher_id)
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        teacher.name = name
        teacher.age = age
        teacher.save()
        return JsonResponse(model_to_dict(teacher))

    def delete(self, request, teacher_id):
        teacher = Teacher.objects.get(pk=teacher_id)
        teacher.delete()
        return JsonResponse({'message': 'Teacher deleted successfully'}, status=204)


# using DRF
# class PersonListCreateView(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        # Your custom logic here
        # For example, you can modify the request data before saving the instance
        request.data['name'] +=" extra"

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def post(self, request):
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                book = serializer.save()  # Save the book instance first
                print(book)
                # Associate authors with the book using many-to-many relationship
                if 'author' in request.data:
                    author_ids = request.data['author']
                    book.author.set(author_ids)  # Set the many-to-many relationship
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

 