from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from yboga.forms.game_add_form import GameAddForm
from yboga.models.game.game import Game
from yboga.models.game.game_component import GameComponent
from yboga.models.game.game_image import GameImage

GameImageFormSet = inlineformset_factory(
    Game,
    GameImage,
    fields=("image", "caption"),
    extra=3,  # можно менять, сколько сразу видно
    can_delete=True,
)

GameComponentFormSet = inlineformset_factory(
    Game, GameComponent, fields=("name", "quantity", "image"), extra=3, can_delete=True
)


def add_game(request):
    if request.method == "POST":
        form = GameAddForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            image_formset = GameImageFormSet(request.POST, request.FILES, instance=game)
            component_formset = GameComponentFormSet(
                request.POST, request.FILES, instance=game
            )

            if image_formset.is_valid() and component_formset.is_valid():
                image_formset.save()
                component_formset.save()
                return redirect("index")
        else:
            image_formset = GameImageFormSet(request.POST, request.FILES)
            component_formset = GameComponentFormSet(request.POST, request.FILES)
    else:
        form = GameAddForm()
        image_formset = GameImageFormSet()
        component_formset = GameComponentFormSet()

    return render(
        request,
        "article_add_form.html",
        {
            "form": form,
            "image_formset": image_formset,
            "component_formset": component_formset,
            "title": "Добавить игру",
        },
    )
