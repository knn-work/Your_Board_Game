from django.shortcuts import render, get_object_or_404

from yboga.models.category import Category


# Create your views here.
def index(request):
    context = {
        "title": "Главная страница",
    }
    return render(request=request, context=context, template_name="index.html")


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
def categories_view(request):
    categories = Category.objects.all()
    context = {"title": "Категории", "categories": categories}
    return render(request=request, context=context, template_name="categories.html")
