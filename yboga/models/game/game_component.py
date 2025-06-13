from django.db import models

from yboga.models.game.game import Game


class GameComponent(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="components", verbose_name="Игра"
    )
    name = models.CharField(max_length=255, verbose_name="Название компонента")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    image = models.ImageField(upload_to="games/components/", blank=True, null=True)

    class Meta:
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты игры"

    def __str__(self):
        return f"{self.name} ×{self.quantity}"
