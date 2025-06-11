from django.db import models

from .category import Category


class Post(models.Model):
    """
    Для новостных постов
    """

    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(
        default="Скоро тут будет постик..", verbose_name="Текст поста"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    photo = models.ImageField(
        upload_to="photo/", blank=True, null=True, verbose_name="Прикрепленное фото "
    )
    watched_count = models.IntegerField(default=0, verbose_name="Просмотры 👀")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Пост"  # Единичное число
        verbose_name_plural = "Посты"  # Множественные числа
