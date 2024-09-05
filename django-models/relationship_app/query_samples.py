#To query all books by a specific author
author_name = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author_name)

#To list all books in a library
library_name = "Library Name"
library = Book.objects.get(library=library_name)
books_in_library=library.books.all()

#To retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = library.librarian