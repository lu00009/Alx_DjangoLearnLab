from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=20)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  def _str_(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=20)
  books = models.ManyToManyField(Book)
  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=20)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)
  def _str_(self):
    return self.name

