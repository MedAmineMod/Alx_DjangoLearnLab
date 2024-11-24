from django.shortcuts import render
from .models import Book , Library
from django.views.generic import DetailView

# Create your views here.



def book_list(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
   
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object() # Retrieve the current book instance
        context['library'] = library
        return  context
