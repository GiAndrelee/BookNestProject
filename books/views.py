from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Shelf, Book
from .forms import ShelfForm, BookForm
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shelves')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('home')
@login_required
def shelves(request):
    user_shelves = Shelf.objects.filter(user=request.user)
    return render(request, 'shelves.html', {'shelves': user_shelves})
@login_required
def add_shelf(request):
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            shelf = form.save(commit=False)
            shelf.user = request.user
            shelf.save()
            return redirect('shelves')
    else:
        form = ShelfForm()
    return render(request, 'shelf_form.html', {'form': form})
@login_required
def edit_shelf(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id, user=request.user)
    if request.method == 'POST':
        form = ShelfForm(request.POST, instance=shelf)
        if form.is_valid():
            form.save()
            return redirect('shelves')
    else:
        form = ShelfForm(instance=shelf)
    return render(request, 'shelf_form.html', {'form': form})
@login_required
def delete_shelf(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id, user=request.user)
    shelf.delete()
    return redirect('shelves')
@login_required
def books(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id, user=request.user)
    books = shelf.books.all()
    return render(request, 'books.html', {'books': books, 'shelf': shelf})
@login_required
def add_book(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.shelf = shelf
            book.save()
            return redirect('books', shelf_id=shelf_id)
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})
@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, shelf__user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books', shelf_id=book.shelf.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, shelf__user=request.user)
    book.delete()
    return redirect('books', shelf_id=book.shelf.id)
