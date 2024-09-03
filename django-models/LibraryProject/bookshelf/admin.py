from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the admin interface
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
