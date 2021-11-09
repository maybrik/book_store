from django.contrib import admin

from .models import Author, Book


class AuthorInline(admin.TabularInline):
    model = Author


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "birthdate", "about"]
    list_filter = ["last_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["name", "description", "price", "author", "genre", "rating", "available"]
    list_filter = ["price", "rating"]
    filter_horizontal = ["author"]