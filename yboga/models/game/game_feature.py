from django.db import models

from .game import Game


class GameFeature(models.Model):
    """
    Модель особенности игры: например, кооперативность, длительность, и т.д.
    """

    game = models.ForeignKey(Game, related_name="features", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.game.title})"

    class Meta:
        verbose_name = "Особенность"
        verbose_name_plural = "Особенности"
