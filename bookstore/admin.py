# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, AuthorsBooks, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publisher", "published_year")
    raw_id_fields = ("authors",)


@admin.register(AuthorsBooks)
class AuthorsBooksAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "book", "contribution_date")
    list_filter = ("contribution_date",)
