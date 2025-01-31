from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, through="AuthorsBooks")
    publisher = models.CharField(max_length=200)
    published_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class AuthorsBooks(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contribution_date = models.DateField()

    def __str__(self):
        return f"{self.author.name} contributed to {self.book.title}"
