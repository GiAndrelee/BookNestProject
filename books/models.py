from django.db import models
from django.contrib.auth.models import User
class Shelf(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelves')
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title
