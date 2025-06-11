from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Категория новостей
    """

    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"  # Единичное число
        verbose_name_plural = "Категории"  # Множественные числа
