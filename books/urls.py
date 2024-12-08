from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('shelves/', views.shelves, name='shelves'),
    path('shelves/add/', views.add_shelf, name='add_shelf'),
    path('shelves/<int:shelf_id>/edit/', views.edit_shelf, name='edit_shelf'),
    path('shelves/<int:shelf_id>/delete/', views.delete_shelf, name='delete_shelf'),
    path('shelves/<int:shelf_id>/books/', views.books, name='books'),
    path('shelves/<int:shelf_id>/books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
