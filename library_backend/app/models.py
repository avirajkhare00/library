from django.db import models

# Create your models here.

class Shelf(models.Model):
  space_in_cm = models.IntegerField()

  def __repr__(self):
    return self.pk

  @classmethod
  def free_space(cls):
    total_space_in_cm = 0
    total_books_space_in_cm = 0
    remaining_space = 0
    for shelf in Shelf.objects.all():
      total_space_in_cm += shelf.space_in_cm
    for book in Book.objects.all():
      total_books_space_in_cm += book.space_in_cm
    return total_space_in_cm - total_books_space_in_cm


class Book(models.Model):
  name = models.CharField(max_length=200)
  space_in_cm = models.IntegerField()
  price = models.IntegerField()

  def __repr__(self):
    return self.name

  @classmethod
  def total_book_price(cls):
    total_price = 0
    for book in Book.objects.all():
      total_price += book.price
    return total_price


class Catalogue(models.Model):
  shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __repr__(self):
    return self.pk

  @classmethod
  def total_books(cls, shelf_id):
    return len(Catalogue.objects.filter(shelf__id=shelf_id))

  @classmethod
  def total_books_price(cls, shelf_id):
    total_price = 0
    for i in Catalogue.objects.filter(shelf__id=shelf_id):
      total_price += i.book.price
    return total_price
