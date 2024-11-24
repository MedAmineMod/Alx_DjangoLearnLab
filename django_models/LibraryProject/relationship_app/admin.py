from django.contrib import admin
from .models import Book , Author, Librarian , Library
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
       
  
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # search_fields = ('title', 'author')
    # list_filter = ('title' , 'author')

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Library , LibraryAdmin)
admin.site.register(Book , BookAdmin)
admin.site.register(Author , AuthorAdmin)
admin.site.register(Librarian , LibrarianAdmin)
