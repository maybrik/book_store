from django.shortcuts import render

from django.views import generic

from .models import Book, Author
from .mixins import CacheMixin

from cart.forms import CartAddProductForm


def index(request):
    num_books = Book.objects.all().count()
    num_books_available = Bookobjects.filter(status__exact='available').count()
    num_authors = Author.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances_available': num_books_available, 'num_authors': num_authors},)


class AuthorListView(generic.ListView, CacheMixin):
    model = Author
    paginate_by = 20


class AuthorDetailView(generic.DetailView, CacheMixin):
    model = Author


class BookListView(generic.ListView, CacheMixin):
    model = Book
    paginate_by = 20


# class BookDetailView(generic.DetailView, CacheMixin):
#    model = Book


def book_detail(request, id):
    book = get_object_or_404(Book, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/book_detail.html', {'book': book,
                                                        'cart_product_form': cart_product_form})
