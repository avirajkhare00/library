from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Shelf, Book, Catalogue
from .serializers import ShelfSerializer, BookSerializer, CatalogueSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_shelf(request, pk):
  try:
    shelf = Shelf.objects.get(pk=pk)
  except Shelf.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single shelf
  if request.method == 'GET':
    serializer = ShelfSerializer(shelf)
    return Response(serializer.data)
  # delete a single shelf
  elif request.method == 'DELETE':
    shelf.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  # update details of a single shelf
  elif request.method == 'PUT':
    serializer = ShelfSerializer(shelf, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_shelves(request):
  # get all shelves
  if request.method == 'GET':
    shelves = Shelf.objects.all()
    serializer = ShelfSerializer(shelves, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    # insert a new record for a shelf
    data = {
      'space_in_cm': request.data.get('space_in_cm')
    }
    serializer = ShelfSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_book(request, pk):
  try:
    book = Book.objects.get(pk=pk)
  except Book.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single book
  if request.method == 'GET':
    serializer = BookSerializer(book)
    return Response(serializer.data)
  # delete a single book
  elif request.method == 'DELETE':
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  # update details of a single book
  elif request.method == 'PUT':
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_books(request):
  # get all books
  if request.method == 'GET':
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    # insert a new record for a book
    data = {
      'name': request.data.get('name'),
      'space_in_cm': request.data.get('space_in_cm'),
      'price': request.data.get('price')
    }
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_catalogue(request, pk):
  try:
    catalogue = Catalogue.objects.get(pk=pk)
  except Catalogue.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single catalogue
  if request.method == 'GET':
    serializer = CatalogueSerializer(catalogue)
    return Response(serializer.data)
  # delete a single catalogue
  elif request.method == 'DELETE':
    catalogue.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  # update details of a single catalogue
  elif request.method == 'PUT':
    serializer = CatalogueSerializer(catalogue, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_catalogues(request):
  # get all catalogue
  if request.method == 'GET':
    catalogue = Catalogue.objects.all()
    serializer = CatalogueSerializer(catalogue, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    # insert a new record for a catalogue
    data = {
      'shelf': request.data.get('shelf'),
      'book': request.data.get('book')
    }
    serializer = CatalogueSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
