from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView,TeacherListView
from .views import BookListCreateView, BookRetrieveUpdateDeleteView
from .views import AuthorListCreateView, AuthorRetrieveUpdateDeleteView

urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonRetrieveUpdateDeleteView.as_view(), name='person-retrieve-update-delete'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDeleteView.as_view(), name='author-retrieve-update-delete'),
      path('teachers/', TeacherListView.as_view(), name='teacher-list'),
      path('teachers/<int:teacher_id>/', TeacherListView.as_view(), name='teacher-detail'),

]
