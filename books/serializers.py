from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AvailableBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('author', 'title', 'release_date')
