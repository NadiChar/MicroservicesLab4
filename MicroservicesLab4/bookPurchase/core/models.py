from django.db import models

# Create your models here.

class bookPurchased(models.Model):
        bookName = models.CharField(max_length=200)

