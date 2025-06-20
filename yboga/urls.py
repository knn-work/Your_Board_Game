from django.urls import path

from yboga.views.forms.user_add_game_form import add_game
from yboga.views.views import (
    index,
    categories_view,
    category_detail,
    game_detail,
    about,
    publishers_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("category/<slug:slug>/", category_detail, name="category_detail"),
    path("game/<slug:slug>/", game_detail, name="game_detail"),
    path("categories", categories_view, name="categories"),
    path("publishers", publishers_view, name="publishers"),
    path("add_game", add_game, name="add_game"),
    path("about", about, name="about"),
]
