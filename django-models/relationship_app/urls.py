from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/', views.BookDetailView.as_view(), name='BookDetailView' )
]
