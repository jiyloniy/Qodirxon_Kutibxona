from django.shortcuts import render
from django.views.generic import ListView
import os
from book.models import Book, Category, Author, Audio, Banner
from datetime import datetime, timedelta, timezone


def home(request):
    banner = Banner.objects.filter(is_active=True)
    # random_book = Book.objects.filter(created_at__gte=datetime.now(timezone.utc) - timedelta(days=10)).order_by('?')[:10]
    #
    random_book = Book.objects.all()
    context = {
        'banner': banner,
        'book': random_book,
    }
    return render(request, 'index-6.html', context)



def me(request):
    return render(request,'free-a-quote.html')

# class BookListView(ListView):
#     model = Book
#     template_name = 'allbook.html'
#     context_object_name = 'books'
#     paginate_by = 6
#
# #    filter by category and author subcategory
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['authors'] = Author.objects.all()
#         context['books'] = Book.objects.all()
#         return context

def category(request, pk):
    books = Book.objects.filter(category__pk=pk)
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'authors': authors,
    }
    return render(request, 'allbook.html', context)

def BookListView(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'authors': authors,
    }
    return render(request, 'allbook.html', context)
def author(request, pk):
    books = Book.objects.filter(author__pk=pk)
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'authors': authors,
    }
    return render(request, 'allbook.html', context)


def book_detail(request, pk):
    book = Book.objects.get(unique_id=pk)
    context = {
        'book': book,
    }
    return render(request, 'qalbiffati.html', context)


def contact(request):
    return render(request, 'free-a-quote.html')

def get_pdf(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'template_html':os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'default-book-view.html')
    }
    return render(request, 'index.html', context)