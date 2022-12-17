from django.db import models

# Create your models here.

class bookList(models.Model):
        bookName = models.CharField(max_length=200)
        authorName = models.CharField(max_length=200)
        BookPrice = models.CharField(max_length=200)
        Type = models.CharField(max_length=200)
