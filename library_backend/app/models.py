from django.db import models

# Create your models here.

class Shelf(models.Model):
  space_in_cm = models.IntegerField()

  def __repr__(self):
    return self.id


class Book(models.Model):
  name = models.CharField(max_length=200)
  space_in_cm = models.IntegerField()
  price = models.IntegerField()

  def __repr__(self):
    return self.name


class Catalogue(models.Model):
  shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __repr__(self):
    return str(shelf.id) + '-' + book.name

  @classmethod
  def total_books(cls, shelf_id):
    return len(Catalogue.objects.filter(shelf__id=shelf_id))

  @classmethod
  def total_books_price(cls, shelf_id):
    total_price = 0
    for i in Catalogue.objects.filter(shelf__id=shelf_id):
      total_price += i.book.price
    return total_price
