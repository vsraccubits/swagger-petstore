from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    Model to store category details.
    """

    name = models.CharField(max_length=100, verbose_name=_("Category Name"))

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Model to store tag details.
    """

    name = models.CharField(max_length=100, verbose_name=_("Tag Name"))

    def __str__(self):
        return self.name


class PhotoUrl(models.Model):
    """
    Model to store pet photo urls.
    """

    photo = models.ImageField(upload_to="photo", verbose_name=_("Photo"))

    def __str__(self):
        filename = self.photo.name.split("/").pop()
        return filename


class Pet(models.Model):
    """
    Model to store pet details.
    """

    class PetStatuses(models.TextChoices):
        AVAILABLE = "available", _("Available")
        PENDING = "pending", _("Pending")
        SOLD = "sold", _("Sold")

    name = models.CharField(max_length=100, verbose_name=_("Pet Name"))
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name=_("Pet Category")
    )
    photo_urls = models.ManyToManyField(PhotoUrl, verbose_name=_("Pet Photo Urls"))
    tags = models.ManyToManyField(Tag, verbose_name=_("Pet Tags"))
    status = models.CharField(
        max_length=30,
        choices=PetStatuses.choices,
        default=PetStatuses.AVAILABLE,
        verbose_name=_("Pet Status"),
    )

    def __str__(self):
        return self.name
