from faker import Faker
from django.core.management.base import BaseCommand
from library.models import Reader
import random


class Command(BaseCommand):
    help = "Migrates employees security license numbers to the new schema"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(200):
            result = random.randrange(0, 2)
            if result:
                name = fake.name_female()
            else:
                name = fake.name_male()
            new_user = name.replace(" ", ".")
            email = f"{new_user}@mail.com"
            reader = new_user.lower()
            user, created = Reader.objects.get_or_create(reader=reader, email=email)
            if created:
                user.save()
