#To query all books by a specific author
author_name="Author Name"
books_by_author = Author.objects.get(name= author_name)
books_by_author = Book.objects.filter(author=author)

#To list all books in a library
library_name = "Library Name"
library = Book.objects.get(library=library_name)
books_in_library=library.books.all()

#To retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = library.librarian