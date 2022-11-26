from django.forms import ModelForm
from .models import Board, Books, BookContents


class BoardForm(ModelForm):

    class Meta:
        model = Board
        fields = [
            "title",
            "content",
        ]


class BooksForm(ModelForm):

    class Meta:
        model = Books
        fields = [
            "title",
            "sub_title",
            "product_id",
            "version_number",
            "book_writer",
        ]


class BookContentsForm(ModelForm):

    class Meta:
        model = BookContents
        fields = (
            "board",
            "order_number",
            "order_name",
        )
