from django.db import models

from .game import Game


class GameImage(models.Model):
    """
    Модель изображения (скриншота) для игры.
    """

    game = models.ForeignKey(Game, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="games/images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"Изображение для {self.game.title}"
