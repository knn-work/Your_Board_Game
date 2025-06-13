from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Категория игр (можно привязать к нескольким играм)
    """

    title = models.CharField(max_length=255, verbose_name="Название", unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name="Слаг", unique=True, blank=True
    )
    description = models.TextField(
        max_length=255, verbose_name="Описание", default="Тут что то будет..."
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]  # категории по алфавиту

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
