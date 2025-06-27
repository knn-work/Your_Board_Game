import random

from django.shortcuts import render, get_object_or_404, redirect

from yboga.models.category import Category
from yboga.models.game.game import Game
from yboga.models.publisher import Publisher


# Create your views here.
def index(request):
    games = Game.objects.prefetch_related("categories").all()
    return render(
        request,
        "index.html",
        {
            "games": games,
            "title": "Главная",
        },
    )


def category_detail(request, slug: str):
    """
    Представление для отображения одной категории по слагу и связанных с ней игр.
    """
    category = get_object_or_404(Category, slug=slug)
    games = (
        category.games.all()
    )  # related_name в модели Game: categories = models.ManyToManyField(...)

    context = {
        "title": category.title,
        "category": category,
        "games": games,
    }
    return render(request, "category.html", context)


# Create your views here.
def publishers_view(request):

    publishers = Publisher.objects.prefetch_related("games").all()
    context = {"title": "Издатели игр", "publishers": publishers}
    return render(request=request, context=context, template_name="publishers.html")


# Create your views here.
def categories_view(request):
    categories = Category.objects.all()
    context = {"title": "Категории", "categories": categories}
    return render(request=request, context=context, template_name="categories.html")


def game_detail(request, slug: str):
    """
    Детальная страница игры по slug.
    """
    game = get_object_or_404(Game, slug=slug)
    context = {
        "game": game,
        "title": game.title,
    }
    return render(request, "game_detail.html", context)


def about(request):
    return render(
        request,
        "about.html",
        {
            "title": "О нас",
        },
    )


def random_game(request):
    """
    Выбирает случайную игру и делает редирект на её страницу.
    """
    slugs = Game.objects.values_list("slug", flat=True)
    if not slugs:
        # Можно сделать редирект на главную или страницу с сообщением
        return redirect("index")  # или вернуть 404
    random_slug = random.choice(slugs)

    return redirect("game_detail", slug=random_slug)
