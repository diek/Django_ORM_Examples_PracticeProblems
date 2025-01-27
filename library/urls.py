from django.urls import path

from . import views

urlpatterns = [
    path("fetch-books/", views.fetch_all_books, name="fetch_books"),
    path("book-title-pub-date/", views.fetch_title_pub_date, name="title_pub_date"),
    path("fetch-new-authors/", views.fetch_new_authors, name="fetch_new_authors"),
    path("fetch-A-gt-8/", views.fetch_a_gt_8, name="fetch_a_gt_8"),
    path("fetch-double-aa/", views.fetch_double_aa, name="fetch_double_aa"),
    path("fetch-search-list/", views.fetch_search_list, name="fetch_search_list"),
    path("fetch-join-date/", views.fetch_join_date, name="fetch_join_date"),
    path("fetch-first-ten-pub/", views.fetch_first_ten_pub, name="fetch_first_ten_pub"),
    path("fetch-last-joined/", views.fetch_last_joined, name="fetch_last_joined"),
    path(
        "fetch-last-author-joined/",
        views.fetch_last_author_joined,
        name="fetch_last_author_joined",
    ),
    path("fetch-2013/", views.fetch_2013, name="fetch_2013"),
]
