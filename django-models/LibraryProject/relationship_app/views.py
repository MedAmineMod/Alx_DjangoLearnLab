from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  , AuthenticationForm 
from django.urls import  reverse_lazy
from django.contrib.auth import login


# Create your views here.



def list_books(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
   
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object # Retrieve the current book instance
        context['library'] = library
        return  context


def register(request):

    form_class = UserCreationForm()
    # success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"
    return render(request, template_name, {'form': form_class})


def login(request):

    form_class = AuthenticationForm()
    # success_url = reverse_lazy("login")
    template_name = "relationship_app/login.html"
    return render(request, template_name, {'form': form_class})



def logout(request):

    
    # success_url = reverse_lazy("login")
    template_name = "relationship_app/logout.html"
    return render(request, template_name )

