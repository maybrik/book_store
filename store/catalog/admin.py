from django.contrib import admin

from .models import Author, Book


class AuthorInline(admin.TabularInline):
    model = Author


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["last_name", "birthdate"]
    list_filter = ["last_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ["price", "rating"]
    filter_horizontal = ["author"]