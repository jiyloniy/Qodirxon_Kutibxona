from django.contrib import admin

from book.models import Category,  Author, Book, Contact, Audio,Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'is_active', 'tag', 'tur')
    list_filter = ('is_active', 'tag', 'tur')
    search_fields = ('name', 'tag', 'tur')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']
    search_fields =[('name', 'is_active')]






@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)


# audio stack admin
class AudioInline(admin.StackedInline):
    model = Audio
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',  'author', 'is_active','unique_id')
    list_filter = ('is_active', 'category',  'author')
    search_fields = ('name', 'category__name',  'author__name')
    inlines = [AudioInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('book', 'file', 'is_active')
    search_fields = ('book__name',)
    list_filter = ('is_active',)
