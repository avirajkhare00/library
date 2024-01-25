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
    ),
    re_path(
        r'^api/v1/catalogue/(?P<pk>[0-9]+)$',
        views.get_update_delete_catalogue,
        name='get_update_delete_catalogue'
    ),
    re_path(
        r'^api/v1/catalogues/$',
        views.get_post_catalogues,
        name='get_post_catalogues'
    ),
    re_path(
        r'^api/v1/analytics/$',
        views.get_analytics,
        name='get_analytics'
    )
]
