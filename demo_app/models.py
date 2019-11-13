from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    booktype = models.CharField(max_length=10)
    introduction = models.TextField()

    """def __str__(self):
        return [self.title, self.author, self.booktype, self.introduction]
    """