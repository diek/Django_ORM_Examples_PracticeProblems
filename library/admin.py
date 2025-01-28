# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Reader, Book, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "address",
        "zipcode",
        "telephone",
        "recommended_by",
        "join_date",
        "popularity_score",
    )
    list_filter = ("join_date",)
    raw_id_fields = ("recommended_by",)


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("id", "reader", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "genre",
        "price",
        "published_date",
        "author",
        "publisher",
    )
    list_filter = ("published_date",)
    raw_id_fields = ("author", "publisher")


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "publishing_company",
        "recommended_by",
        "join_date",
        "popularity_score",
    )
    list_filter = ("join_date",)
    raw_id_fields = ("recommended_by",)
