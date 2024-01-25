from rest_framework import serializers
from .models import Shelf, Book, Catalogue


class ShelfSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shelf
    fields = ('id', 'space_in_cm')


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('id', 'name', 'space_in_cm', 'price')


class CatalogueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Catalogue
    fields = ('id', 'shelf', 'book')
