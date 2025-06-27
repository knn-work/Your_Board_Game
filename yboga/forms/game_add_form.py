from django import forms

from yboga.models.game.game import Game


class GameAddForm(forms.ModelForm):
    """
    Форма для добавления новой игры пользователем.
    """

    class Meta:
        model = Game
        fields = (
            "title",
            "slug",
            "image",
            "description",
            "release_date",
            "min_players",
            "max_players",
            "categories",
            "publisher",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название игры"}
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "slug (можно оставить пустым)",
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Описание"}
            ),
            "release_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "min_players": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Минимум игроков"}
            ),
            "max_players": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Максимум игроков"}
            ),
            "categories": forms.SelectMultiple(attrs={"class": "form-select"}),
            "publisher": forms.Select(attrs={"class": "form-select"}),
        }
