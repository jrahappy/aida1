from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Board(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)
