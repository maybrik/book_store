from .models import Author, Book, Publisher, BookInstance

from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "birth_date", "about"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "price", "author"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["publisher_name", "city", "license"]


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ["name", "publisher_name", "isbn", "date_of_order", "status"]
        