from typing import Any

from django.db import models
from django.utils.text import slugify

from yboga.models.category import Category
from yboga.models.publisher import Publisher


class Game(models.Model):
    """
    Модель основной игры.

    Хранит данные об изображении, названии, описании, дате выхода,
    связанных категориях и временных метках создания/обновления.
    """

    image = models.ImageField(
        upload_to="games/images/", verbose_name="Обложка", blank=True, null=True
    )
    title = models.CharField(max_length=255, verbose_name="Название", unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name="Слаг", unique=True, blank=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    release_date = models.DateField(verbose_name="Дата выхода", null=True, blank=True)
    categories = models.ManyToManyField(
        Category, related_name="games", verbose_name="Категории"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="games",
        verbose_name="Издатель",
    )

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ["title"]

    def __str__(self) -> str:
        """Возвращает строковое представление игры."""
        return self.title

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Автоматически генерирует slug, если он не указан."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
