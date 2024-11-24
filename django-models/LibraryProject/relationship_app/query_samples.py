from relationship_app.models import Book, Author, Librarian ,Library

author_name = "amine"

author =  Author.objects.get(name=author_name)

books = Book.objects.filter(author=author)

for book in books :
    print(book.name , book.id)


library_name = "Ohod"

library_object = Library.objects.get(name=library_name)

for book in library_object.books.all() :
    print(book.name , book.id)



librarian_name_library = Librarian.objects.get(library = library_object.id).name











