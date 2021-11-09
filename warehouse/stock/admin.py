from django.contrib import admin

from .models import Author, Book, BookInstance, Publisher


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    fk_name = "name"
    fk_name2 = "publisher_name"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "birthdate", "about"]
    list_filter = ["last_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["name", "price", "author"]
    list_filter = ["price"]
    filter_horizontal = ["author"]
    inlines = [BookInstanceInline]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ["publisher_name", "city", "license",]
    list_filter = ["publisher_name"]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    fields = ["name", "isbn", "publisher_name", "date_of_order", "status"]
    list_filter = ["isbn"]
