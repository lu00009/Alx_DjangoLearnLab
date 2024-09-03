#create

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

#output
<bookshelf.models.Book: 1984>

#Retrieve

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

#output

1984 George Orwell 1949

#update

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

#output

<bookshelf.models.Book: Nineteen Eighty-Four>

#delete

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

#output

(1, {'bookshelf.Book': 1})