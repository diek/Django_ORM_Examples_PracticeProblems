from faker import Faker
from django.core.management.base import BaseCommand
from library.models import Publisher
import random


fake = Faker()


class Command(BaseCommand):
    help = "Migrates employees security license numbers to the new schema"

    def handle(self, *args, **options):
        def generate_publishers(num_publishers=100):
            # Create publishers that reference others
            publishers = Publisher.objects.all()

            for publisher in publishers:
                publisher.recommended_by = random.choice(publishers)
                publisher.save()

        # Call the function to populate your database
        generate_publishers()
