from django.db import models

from .game import Game


class GameExpansion(models.Model):
    """
    Модель дополнения к игре.
    """

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="expansions",
        verbose_name="Базовая игра",
    )
    title = models.CharField(max_length=255, verbose_name="Название дополнения")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="games/expansions/", blank=True, null=True)
    release_date = models.DateField(blank=True, null=True, verbose_name="Дата выхода")

    class Meta:
        verbose_name = "Дополнение"
        verbose_name_plural = "Дополнения"

    def __str__(self) -> str:
        return f"{self.title} (дополнение к {self.game.title})"
