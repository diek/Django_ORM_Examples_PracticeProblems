# Title,Genre,Price,Published Date
from django.core.management.base import BaseCommand
from library.models import Author, Book, Publisher
import random
from decimal import Decimal


class Command(BaseCommand):
    help = "Migrates employees security license numbers to the new schema"

    def handle(self, *args, **options):
        def get_books():
            authors = Author.objects.all()
            publishers = Publisher.objects.all()
            with open("non_fiction_books.csv", "r") as file:
                next(file)
                for idx, row in enumerate(file):
                    record = row.split(",")
                    book, created = Book.objects.get_or_create(
                        title=record[0],
                        genre=record[1],
                        price=Decimal(record[2]),
                        published_date=record[3],
                        author=random.choice(authors),
                        publisher=random.choice(publishers),
                    )
                    if created:
                        book.save()

            # return companies

        get_books()
