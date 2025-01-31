from django.urls import path

from . import views

urlpatterns = [
    path(
        "fetch-all-related-objects/",
        views.fetch_all_related_objects,
        name="fetch_all_related_objects",
    ),
    path(
        "fetch-by-author-title/",
        views.fetch_by_author_title,
        name="fetch_by_author_title",
    ),
    path(
        "fetch-check-for-existence/",
        views.fetch_check_for_existence,
        name="fetch_check_for_existence",
    ),
]
