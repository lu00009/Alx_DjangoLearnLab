#To query all books by a specific author
specific_author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=specific_author)

#To list all books in a library
specific_library = Library.objects.get(name="Library Name")
books_in_library = Book.objects.filter(library=specific_library)

#To retrieve the librarian for a library
specific_library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=specific_library)