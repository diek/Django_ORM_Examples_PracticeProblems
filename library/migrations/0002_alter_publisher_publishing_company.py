# Generated by Django 3.2.17 on 2025-01-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='publishing_company',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
