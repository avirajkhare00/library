from django.test import TestCase
from .models import Shelf, Book, Catalogue

# Create your tests here.

class ShelfTest(TestCase):

  def test_shelf_space(self):
    shelf_one = Shelf.objects.create(space_in_cm=10)

    self.assertEqual(shelf_one.space_in_cm, 10)

  def test_all_shelf_free_space(self):
    shelf_one = Shelf.objects.create(space_in_cm=10)

    book_one = Book.objects.create(name="Jungle Book", space_in_cm="2", price=100)
    book_two = Book.objects.create(name="Jungle Book Returns", space_in_cm="3", price=150)

    self.assertEqual(Shelf.free_space(), 5)


class BookTest(TestCase):

  def test_book_name_and_price(self):
    book_one = Book.objects.create(name="Jungle Book", space_in_cm="2", price=100)
    book_two = Book.objects.create(name="Jungle Book Returns", space_in_cm="3", price=150)

    self.assertEqual(book_one.name, "Jungle Book")
    self.assertEqual(book_two.name, "Jungle Book Returns")

    self.assertEqual(book_one.price, 100)
    self.assertEqual(book_two.price, 150)

  def test_total_books_price(self):
    book_one = Book.objects.create(name="Jungle Book", space_in_cm="2", price=100)
    book_two = Book.objects.create(name="Jungle Book Returns", space_in_cm="3", price=150)

    self.assertEqual(Book.total_book_price(), 250)


class CatalogueTest(TestCase):
  def test_catalogue_total_books_stored(self):
    shelf_one = Shelf.objects.create(space_in_cm=10)

    book_one = Book.objects.create(name="Jungle Book", space_in_cm="2", price=100)
    book_two = Book.objects.create(name="Jungle Book Returns", space_in_cm="3", price=150)
    book_three = Book.objects.create(name="Gita", space_in_cm="6", price=100)

    catalogue_one = Catalogue.objects.create(shelf=shelf_one, book=book_one)
    catalogue_two = Catalogue.objects.create(shelf=shelf_one, book=book_two)
    catalogue_three = Catalogue.objects.create(shelf=shelf_one, book=book_three)

    self.assertEqual(Catalogue.total_books(shelf_one.id), 3)

  def test_catalogue_total_books_price(self):
    shelf_one = Shelf.objects.create(space_in_cm=10)

    book_one = Book.objects.create(name="Jungle Book", space_in_cm="2", price=100)
    book_two = Book.objects.create(name="Jungle Book Returns", space_in_cm="3", price=150)
    book_three = Book.objects.create(name="Gita", space_in_cm="6", price=100)

    catalogue_one = Catalogue.objects.create(shelf=shelf_one, book=book_one)
    catalogue_two = Catalogue.objects.create(shelf=shelf_one, book=book_two)
    catalogue_three = Catalogue.objects.create(shelf=shelf_one, book=book_three)

    self.assertEqual(Catalogue.total_books_price(shelf_one.id), 350)
