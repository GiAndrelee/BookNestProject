from django import forms
from .models import Shelf, Book
class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ['name']
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'shelf']
