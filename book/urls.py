from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='allbook'),
    path('allbook/', views.BookListView, name='books'),
    path('allbook/category/<int:pk>', views.category, name='category'),
    path('allbook/author/<int:pk>', views.author, name='author'),
    path('allbook/book/<int:pk>', views.book_detail, name='book_detail'),
    #contact
    path('contact/', views.contact, name='contact'),
    path('pdf/<int:pk>', views.get_pdf, name='pdf'),
]
