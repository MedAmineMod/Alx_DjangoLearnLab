from django.db import models

# Create your models here.

class Author(models.Model): 
    name  =  models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model): 

    title = models.CharField(max_length=200)
    author = models.ForeignKey(to=Author , on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"  



class Library(models.Model):

   name = models.CharField(max_length=200)
   books =  models.ManyToManyField(to=Book)

class Librarian(models.Model):

    name = models.CharField(max_length=200)
    library = models.OneToOneField(to=Library , on_delete=models.CASCADE)
