from django.db import models
from django.utils.text import slugify


class WebContent(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    markdown_content = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)
