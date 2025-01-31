from django.shortcuts import render

from django.db.models import Q, F, Count, Avg, Sum, Max, Min
from bookstore.models import Author, Book


def fetch_all_related_objects(request):
    book = Book.objects.get(pk=23)
    book_authors = book.authors.all()
    problem = "1. Querying All Related Objects."
    context = {"book": book, "book_authors": book_authors, "problem": problem}
    return render(request, "bookstore/fetch-all-related-objects.html", context)


def fetch_by_author_title(request):
    keegan_books = Book.objects.filter(authors__name__startswith="John K")
    american_sniper = Author.objects.filter(books__title="American Sniper")
    problem = "2. Filtering Related Objects\nYou can filter related objects based on certain conditions"
    context = {
        "keegan_books": keegan_books,
        "american_sniper": american_sniper,
        "problem": problem,
    }
    return render(request, "bookstore/fetch-by-author-title.html", context)


def fetch_check_for_existence(request):
    book1 = Book.objects.get(pk=23)
    # Lynn Picknett
    is_lynn_author = book1.authors.filter(name="Lynn Picknett").exists()
    problem = "3. Checking for Existence Using exists()."
    context = {"book1": book1, "is_lynn_author": is_lynn_author, "problem": problem}
    return render(request, "bookstore/fetch-check-for-existence.html", context)
