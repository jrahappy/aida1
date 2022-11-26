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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)


class Books(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    sub_title = models.CharField(max_length=250)
    product_id = models.IntegerField(default=0)
    version_number = models.CharField(max_length=50)
    book_writer = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, allow_unicode=True, null=True, blank=True)
    # cover_image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)


class BookContents(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.SET_DEFAULT, default=0)
    #board = models.IntegerField(default=0)
    order_number = models.IntegerField(default=0)
    order_name = models.CharField(max_length=100)
