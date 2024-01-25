from django.urls import re_path
from . import views


urlpatterns = [
    re_path(
        r'^api/v1/shelf/(?P<pk>[0-9]+)$',
        views.get_update_delete_shelf,
        name='get_update_delete_shelf'
    ),
    re_path(
        r'^api/v1/shelves/$',
        views.get_post_shelves,
        name='get_post_shelves'
    ),
    re_path(
        r'^api/v1/book/(?P<pk>[0-9]+)$',
        views.get_update_delete_book,
        name='get_update_delete_book'
    ),
    re_path(
        r'^api/v1/books/$',
        views.get_post_books,
        name='get_post_books'
    )
]
