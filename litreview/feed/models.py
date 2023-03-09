from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image


class Ticket(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (100, 100)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        if self.image:
            super().save(*args, **kwargs)
            self.resize_image()
        else:
            super().save(*args, **kwargs)


class Review(models.Model):
    objects = models.Manager()

    # OneToOneField because one review for one ticket
    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        related_name='ticket_review',
        primary_key=False
    )
    rating = models.PositiveSmallIntegerField(
       validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
