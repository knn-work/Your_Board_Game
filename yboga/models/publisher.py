from django.db import models


class Publisher(models.Model):
    """
    Издатель игры.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    website = models.URLField(blank=True, verbose_name="Сайт")
    logo = models.ImageField(upload_to="publishers/logos/", blank=True, null=True)

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
