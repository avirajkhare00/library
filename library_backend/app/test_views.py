import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Shelf, Book, Catalogue
from .serializers import ShelfSerializer, BookSerializer, CatalogueSerializer


# initialize the APIClient app
client = Client()


class GetAllShelfTest(TestCase):

  def setUp(self):
    Shelf.objects.create(space_in_cm=10)
    Shelf.objects.create(space_in_cm=12)
    Shelf.objects.create(space_in_cm=15)

  def test_get_all_shelves(self):
    # get API response
    response = client.get(reverse('get_post_shelves'))
    # get data from db
    shelves = Shelf.objects.all()
    serializer = ShelfSerializer(shelves, many=True)

    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleShelfTest(TestCase):

  def setUp(self):
    self.shelf_one = Shelf.objects.create(space_in_cm=10)
    self.shelf_two = Shelf.objects.create(space_in_cm=15)

  def test_get_valid_single_shelf(self):
    response = client.get(
            reverse('get_update_delete_shelf', kwargs={'pk': self.shelf_one.pk}))
    shelf_one = Shelf.objects.get(pk=self.shelf_one.pk)
    serializer = ShelfSerializer(shelf_one)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_invalid_single_shelf(self):
    response = client.get(
            reverse('get_update_delete_shelf', kwargs={'pk': 15}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewShelfTest(TestCase):
  def setUp(self):
    self.valid_payload = {'space_in_cm': 5}
    self.invalid_payload = {'space': 10}

  def test_create_valid_shelf(self):
    response = client.post(
      reverse('get_post_shelves'),
      data = json.dumps(self.valid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_create_invalid_shelf(self):
    response = client.post(
      reverse('get_post_shelves'),
      data = json.dumps(self.invalid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleShelfTest(TestCase):
  def setUp(self):
    self.shelf_one = Shelf.objects.create(space_in_cm='5')
    self.valid_payload = {'space_in_cm': 10}
    self.invalid_payload = {'space': 15}

  def test_update_valid_shelf(self):
    response = client.put(
      reverse('get_update_delete_shelf', kwargs = {'pk': self.shelf_one.pk}),
      data = json.dumps(self.valid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_update_invalid_shelf(self):
    response = client.put(
      reverse('get_update_delete_shelf', kwargs = {'pk': self.shelf_one.pk}),
      data = json.dumps(self.invalid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleShelfTest(TestCase):
  def setUp(self):
    self.shelf_one = Shelf.objects.create(space_in_cm=10)
    self.shelf_two = Shelf.objects.create(space_in_cm=15)

  def test_valid_delete_shelf(self):
    response = client.delete(reverse('get_update_delete_shelf', kwargs={'pk': self.shelf_one.pk}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_invalid_delete_shelf(self):
    response = client.delete(reverse('get_update_delete_shelf', kwargs={'pk': 15}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAllBooksTest(TestCase):

  def setUp(self):
    Book.objects.create(name='Gita', space_in_cm=4, price=50)
    Book.objects.create(name='Hanuman Chalisa', space_in_cm=2, price=10)
    Book.objects.create(name='Ramayana', space_in_cm=8, price=200)

  def test_get_all_books(self):
    # get API response
    response = client.get(reverse('get_post_books'))
    # get data from db
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleBookTest(TestCase):

  def setUp(self):
    self.book_one = Book.objects.create(name='Gita', space_in_cm=4, price=50)
    self.book_two = Book.objects.create(name='Ramayana', space_in_cm=8, price=200)

  def test_get_valid_single_book(self):
    response = client.get(
            reverse('get_update_delete_book', kwargs={'pk': self.book_one.pk}))
    book_one =Book.objects.get(pk=self.book_one.pk)
    serializer = BookSerializer(book_one)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_invalid_single_book(self):
    response = client.get(
            reverse('get_update_delete_book', kwargs={'pk': 15}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBookTest(TestCase):
  def setUp(self):
    self.valid_payload = {'name': 'Gita', 'space_in_cm': 4, 'price': 50}
    self.invalid_payload = {'space': 10}

  def test_create_valid_book(self):
    response = client.post(
      reverse('get_post_books'),
      data = json.dumps(self.valid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_create_invalid_book(self):
    response = client.post(
      reverse('get_post_books'),
      data = json.dumps(self.invalid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleBookTest(TestCase):
  def setUp(self):
    self.book_one = Book.objects.create(name='Gita', space_in_cm=4, price=50)
    self.valid_payload = {'name': 'Bible', 'space_in_cm': 6, 'price': 100}
    self.invalid_payload = {'space': 15}

  def test_update_valid_book(self):
    response = client.put(
      reverse('get_update_delete_book', kwargs = {'pk': self.book_one.pk}),
      data = json.dumps(self.valid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_update_invalid_book(self):
    response = client.put(
      reverse('get_update_delete_book', kwargs = {'pk': self.book_one.pk}),
      data = json.dumps(self.invalid_payload),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleBookTest(TestCase):
  def setUp(self):
    self.book_one = Book.objects.create(name='Gita', space_in_cm=4, price=50)
    self.book_two = Book.objects.create(name='Ramayana', space_in_cm=8, price=200)

  def test_valid_delete_book(self):
    response = client.delete(reverse('get_update_delete_book', kwargs={'pk': self.book_one.pk}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_invalid_delete_shelf(self):
    response = client.delete(reverse('get_update_delete_book', kwargs={'pk': 15}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
