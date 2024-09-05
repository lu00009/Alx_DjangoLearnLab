from django.shortcuts import render
# Create your views here.
from .models import Book
from django.views.generic import DetailView
from .models import Library
def book_list(request):
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)



class LibraryDetailView(DetailView):
  model = Book
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['books'] = self.objects.books.all() 
    return context