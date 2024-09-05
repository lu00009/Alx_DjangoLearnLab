from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from.views import register
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>//', views.LibraryDetailView.as_view(), name='LibraryDetailView' ),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'relationship_app/login.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
    path('add_book/', views.BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
]
