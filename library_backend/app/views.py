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
