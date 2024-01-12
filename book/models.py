from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta, timezone
from uuid import uuid4
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name




class Author(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to="author/", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.full_name

    @property
    def imgage(self):
        return self.img.url
    @property
    def author_books(self):
        return self.book_set.all().count()

class Book(models.Model):
    unique_id = models.CharField(max_length=100, default=uuid4, editable=False, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="book/", null=True, blank=True, default='default/defaultbook.png')
    file = models.FileField(upload_to="book/")
    muqovasi = (
        ("Yumshoq", "Yumshoq"),
        ("Qattiq", "Qattiq"),
    )
    muqovasi = models.CharField(max_length=100, choices=muqovasi, null=True, blank=True)
    pager = models.CharField(max_length=100, null=True, blank=True)
    printed_year = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    @property
    def img(self):
        return self.image.url

    def __str__(self):
        return self.name

    @property
    def is_new(self):
        now = datetime.now(timezone.utc)
        return (now - self.created_at) < timedelta(days=3)


class Audio(models.Model):
    file = models.FileField(upload_to="audio/")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banner/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    tur = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def img(self):
        return self.image.url


class BannerChild(models.Model):
    image = models.ImageField(upload_to="banner/")

    def __str__(self):
        return self.image.url
