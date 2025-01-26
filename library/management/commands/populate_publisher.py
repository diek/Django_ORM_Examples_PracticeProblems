from faker import Faker
from django.core.management.base import BaseCommand
from library.models import Publisher
import random
from datetime import datetime, timedelta
from django.db import IntegrityError

fake = Faker()


class Command(BaseCommand):
    help = "Migrates employees security license numbers to the new schema"

    def handle(self, *args, **options):
        fake = Faker()

        def get_companies():
            companies = []
            with open("publishers.csv", "r") as file:
                next(file)
                for row in file:
                    record = row.split("|")
                    companies.append(record[0])
            return companies

        def generate_publishers(num_publishers=100):
            # companies = get_companies()
            # publishers = []
            # # First, create some base publishers (without references to others)
            # try:
            #     for idx, _ in enumerate(range(101)):
            #         publisher = Publisher(
            #             publishing_company=companies[idx],
            #             recommended_by=None,
            #             join_date=fake.date_between(
            #                 start_date="-30y", end_date="today"
            #             ),
            #             popularity_score=random.randint(1, 100),
            #         )
            #         publisher.save()
            #         publishers.append(publisher)
            # except IntegrityError as e:
            #     next

            # Now, create publishers that reference others
            publishers = Publisher.objects.all()

            for publisher in publishers:
                print(random.choice(publishers))

        # Call the function to populate your database
        generate_publishers()
