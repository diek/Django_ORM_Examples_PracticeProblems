from django.shortcuts import render
import datetime
from django.db.models import Q, F, Count, Avg, Sum, Max, Min
from .models import Author, Book, Publisher


def fetch_all_books(request):
    all_books = Book.objects.order_by("-title")[:20]
    problem = (
        "1. Query using Django ORM to fetch all the books objects from your database."
    )
    context = {"all_books": all_books, "problem": problem}
    return render(request, "library/fetch-all-books.html", context)


def fetch_title_pub_date(request):
    all_books = Book.objects.all()[:20]
    problem = "2. Query using Django ORM to fetch title and published_date of all books from the database."
    context = {"all_books": all_books, "problem": problem}
    return render(request, "library/fetch-title-pub-date.html", context)


def fetch_new_authors(request):
    new_authors = Author.objects.filter(popularity_score=0)
    problem = "3. Fetch first name and last name of all the new authors.\n(Authors with popularity_score = 0 are new authors )."
    context = {"new_authors": new_authors, "problem": problem}
    return render(request, "library/fetch-new-authors.html", context)


def fetch_a_gt_8(request):
    q1 = Author.objects.filter(popularity_score__gt=8)
    authors = q1.filter(first_name__startswith="A")
    problem = "4. Fetch first name and popularity score of all authors whose first name starts \nwith A and popularity score is greater than or equal to 8."
    context = {"authors": authors, "problem": problem}
    return render(request, "library/fetch-a-8-authors.html", context)


def fetch_double_aa(request):
    authors = Author.objects.filter(first_name__icontains="aa")
    problem = "5. Fetch first name of all the authors with aa case insensitive in their first name."
    context = {"authors": authors, "problem": problem}
    return render(request, "library/fetch-double-aa.html", context)


def fetch_search_list(request):
    list = [1, 3, 23, 43, 134, 25]
    authors = Author.objects.all().filter(pk__in=list)
    problem = "6. Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25]."
    context = {"authors": authors, "problem": problem}
    return render(request, "library/fetch-search-list.html", context)


def fetch_join_date(request):
    authors = (
        Author.objects.filter(join_date__gte="2012-09-01")
        .order_by("join_date")
        .values_list("firstname", "join_date")
    )
    problem = (
        "7. Fetch list of all the publishers who joined after or in September 2012, \n"
    )
    problem += "output list should only contain first name and join date of publisher."
    problem += " \nOrder by join date."
    context = {"authors": authors, "problem": problem}
    return render(request, "library/fetch-join-date.html", context)


def fetch_first_ten_pub(request):
    publishers = Publisher.objects.all().order_by("publishing_company").distinct()[:10]
    problem = "8. Fetch ordered list of first 10 last names of Pubs, no dups."

    context = {"publishers": publishers, "problem": problem}
    return render(request, "library/fetch-first-ten-pub.html", context)


def fetch_last_joined(request):
    last_joined = [
        Author.objects.all().order_by("join_date").last(),
        Publisher.objects.all().order_by("-join_date").first(),
    ]
    problem = "9. Get the signup date for the last joined Author and Publisher."

    context = {"last_joined": last_joined, "problem": problem}
    return render(request, "library/fetch-last-joined.html", context)


def fetch_last_author_joined(request):
    last_author = (
        Author.objects.all()
        .order_by("-join_date")
        .values_list("first_name", "last_name", "join_date")
        .first()
    )
    problem = (
        "10. Get the first name, last name & join date of the last author who joined."
    )
    context = {"last_author": last_author, "problem": problem}
    return render(request, "library/fetch-last-author-joined.html", context)


def fetch_2013(request):
    authors2013 = Author.objects.all().filter(
        join_date__gte=datetime.date(year=2013, month=1, day=1)
    )
    problem = (
        "11. Get the first name, last name & join date of the last author who joined."
    )
    context = {"authors2013": authors2013, "problem": problem}
    return render(request, "library/fetch-2013.html", context)


def fetch_total_price(request):
    books = (
        Book.objects.all()
        .filter(author__popularity_score__gte=7)
        .aggregate(total_book_price=Sum("price"))
    )
    problem = "12. Fetch total price of all the books written by authors with popularity score 7 or higher."
    context = {"books": books, "problem": problem}
    return render(request, "library/fetch-total-price.html", context)


def fetch_books_by_a(request):
    a_authored_books = (
        Book.objects.all()
        .filter(author__first_name__startswith="A")
        .values_list("title", flat=True)
    )
    problem = "13. Fetch list of titles of all books written by authors whose 1st name starts with ‘A’.\n"
    problem += " The result should contain a list of the titles of every book. Not a list of tuples."
    context = {"a_authored_books": a_authored_books, "problem": problem}
    return render(request, "library/fetch-books-by-a.html", context)


def fetch_total_price_authors134(request):
    list = [1, 3, 4]
    # total_price = Book.objects.all().filter(author__pk__in=[1, 3, 4]).aggregate("price")
    specific_authors = Book.objects.all().filter(author__in=list).order_by("author_id")
    total_price = specific_authors.aggregate(total_book_price=Sum("price"))
    problem = "14. Get total price of all the books written by author with pk in list [1, 3, 4]"

    context = {
        "specific_authors": specific_authors,
        "total_price": total_price,
        "problem": problem,
    }
    return render(request, "library/fetch-total-price-authors134.html", context)


def fetch_authors_followers(request):
    authors_recommenders = Author.objects.all()
    problem = "15. Produce a list of all the authors along with their recommender."
    context = {
        "authors_recommenders": authors_recommenders,
        "problem": problem,
    }
    return render(request, "library/fetch-authors-followers.html", context)


def fetch_authors_Penguin(request):
    authors_Penguin = Book.objects.filter(publisher=37).order_by("author__first_name")
    problem = "16. Produce list of all authors who published their book by \n"
    problem += "publisher pk = 37, output list should be ordered by first name."
    context = {
        "authors_Penguin": authors_Penguin,
        "problem": problem,
    }
    return render(request, "library/fetch-authors-Penguin.html", context)


# 17. Create three new users and add in the followers of the author with pk = 1.
# 18. Set the followers list of the author with pk = 2, with only one user.
# 19. Add new users in followers of the author with pk = 1.
# 20. Remove one user from the followers of the author with pk = 1.


# Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing Author.objects manager )
# Fetch list of all authors who wrote a book with “tle” as part of Book Title.
# Fetch the list of authors whose names start with ‘A’ case insensitive, and either their popularity score is greater than 5 or they have joined after 2014. with Q objects.
# Retrieve a specific object with primary key= 1 from the Author table.
# Retrieve the first N=10 records from an Author table.
# Retrieve records from a table that match this condition, popularity score = 7. And get the first and last record of that list.
# Retrieve all authors who joined after or in the year 2012, popularity score greater than or equal to 4, join date after or with date 12, and first name starts with ‘a’ (case insensitive) without using Q objects.
# Retrieve all authors who did not join in 2012.
# Retrieve Oldest author, Newest author, Average popularity score of authors, sum of price of all books in database.
# Retrieve all authors who have no recommender, recommended by field is null.
# Retrieve the books that do not have any authors, where the author is null. Also, retrieve the books whose authors are present, but do not have a recommender, where the author is not null and the author’s recommender is null. (Note that if the condition for the author not being null is not specified and only the condition for the recommender being null is mentioned, all books with both author null and author’s recommender null will be retrieved.)
# Total price of books written by author with primary key = 1. ( Aggregation over related model ), oldest book written by author with pk = 1, latest book written by author with pk = 1.
# Among the publishers in the Publishers table what is the oldest book any publisher has published.
# Average price of all the books in the database.
# Maximum popularity score of publisher among all the publishers who published a book for the author with pk = 1. (Reverse Foreign Key hop)
# Count the number of authors who have written a book which contains the phrase ‘ab’ case insensitive.
# Get all the authors with followers more than 216.
# Get average popularity score of all the authors who joined after 20 September 2014.
# Generate a list of books whose author has written more than 10 books.
# Get the list of books with duplicate titles.
