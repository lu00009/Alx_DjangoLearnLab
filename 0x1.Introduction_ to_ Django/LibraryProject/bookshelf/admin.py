from django.contrib import admin

# Register your models here.
from .models import Book
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('title', 'author', 'published_date')
    
    # Add filters in the admin interface
    list_filter = ('author', 'published_date')
    
    # Add search functionality
    search_fields = ('title', 'author', 'isbn')

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
