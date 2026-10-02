from django.urls import path

from . import views


app_name = "ebooks"


urlpatterns = [
    path(
        "",
        views.ebook_index,
        name="index",
    ),
    path(
        "<slug:slug>/",
        views.ebook_category,
        name="category",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/",
        views.ebook_detail,
        name="detail",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/download/",
        views.ebook_download,
        name="download",
    ),
]