from faker import Faker
from django.core.management.base import BaseCommand
from random import randint, choice
from datetime import date, timedelta
from library.models import Author, Reader
import random


class Command(BaseCommand):
    help = "Migrates employees security license numbers to the new schema"

    def handle(self, *args, **options):
        fake = Faker()

        def create_fake_author():
            # Generate fake data for Author
            first_name = fake.first_name()
            last_name = fake.last_name()
            address = fake.address()
            zipcode = fake.zipcode()
            telephone = fake.phone_number()
            join_date = fake.date_between(start_date="-10y", end_date="today")
            popularity_score = randint(1, 1000)

            # Randomly select a recommended author from the Author table
            recommended_by = (
                Author.objects.order_by("?").first()
                if Author.objects.exists()
                else None
            )

            # Create the Author instance
            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                zipcode=zipcode,
                telephone=telephone,
                join_date=join_date,
                popularity_score=popularity_score,
                recommended_by=recommended_by,
            )

            return author

        def create_fake_reader():
            # Generate fake data for Reader
            reader_name = fake.name()
            email = fake.email()

            # Create the Reader instance
            reader = Reader.objects.create(reader=reader_name, email=email)

            return reader

        def create_fake_data(num_authors=50, num_readers=50):
            # Create Authors and Readers
            authors = [create_fake_author() for _ in range(num_authors)]
            readers = [create_fake_reader() for _ in range(num_readers)]

            # Randomly assign followers to authors (ManyToMany)
            for author in authors:
                # Pick random readers to follow the author
                num_followers = random.randint(5, 20)
                followers = random.sample(readers, num_followers)
                author.followers.add(*followers)

            print(f"Created {num_authors} authors and {num_readers} readers.")

        # Run the function to create fake data
        create_fake_data(num_authors=50, num_readers=50)
