from django.urls import path

from yboga.views import index, categories_view, category_detail

urlpatterns = [
    path("", index),
    path("category/<slug:slug>/", category_detail, name="category_detail"),
    path("categories", categories_view, name="categories"),
]
