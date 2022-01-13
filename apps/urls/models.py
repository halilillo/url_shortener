import string
import random

from django.db import models


class Url(models.Model):
    url = models.URLField("Original url", max_length=1000)
    short_url = models.URLField("Short url", max_length=200)

    def __str__(self):
        return self.short_url

    def save(self):
        if not self.pk:
            self.shorten_url()
        return super().save()

    def shorten_url(self):
        short = ''.join(random.choices(string.ascii_letters, k=6))
        while Url.objects.filter(short_url=short).exists():
            short = ''.join(random.choices(string.ascii_letters, k=6))
        self.short_url = short
