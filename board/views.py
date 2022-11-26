from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.db.models import Q
from .models import Board, Books, BookContents
from .forms import BoardForm, BooksForm, BookContentsForm
from django.core.paginator import Paginator


def Board_list(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    Boards = Board.objects.all()
    if kw:
        Boards = Boards.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()
    paginator = Paginator(Boards, 5)
    page_obj = paginator.get_page(page)

    context = {
        "Boards": page_obj,
        "page": page,
        "kw": kw
    }
    return render(request, "board/list.html", context)


def Board_retrieve(request, pk):
    Post = Board.objects.get(id=pk)
    context = {
        "Post": Post
    }
    return render(request, "board/detail.html", context)


def Board_create(request):
    form = BoardForm()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():

            board = form.save(False)
            board.author = request.user
            board.created = timezone.now()
            board.updated = timezone.now()
            board.save()
            return redirect('board:list')

    context = {
        "form": form
    }
    return render(request, "board/create.html", context)


def Board_update(request, pk):
    Post = Board.objects.get(id=pk)
    form = BoardForm(instance=Post)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=Post)
        if form.is_valid():
            form.save()
            # return render(request, 'board:detail', Post)
            return redirect('board:detail', pk)

    context = {
        "form": form
    }
    return render(request, "board/update.html", context)


def Board_update_done(request, pk):
    Post = Board.objects.get(id=pk)
    form = BoardForm(instance=Post)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=Post)
        if form.is_valid():
            # form.save()
            return redirect('board:list')

    context = {
        "form": form
    }
    return render(request, "board/update.html", context)


def Board_delete(request, pk):
    Post = Board.objects.get(id=pk)
    Post.delete()
    return redirect("/")


def book_list(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    books = Books.objects.filter(is_deleted=False)
    if kw:
        books = books.filter(
            Q(title__icontains=kw) |
            Q(subtitle__icontains=kw)
        ).distinct()
    paginator = Paginator(books, 5)
    page_obj = paginator.get_page(page)

    context = {
        "books": page_obj,
        "page": page,
        "kw": kw
    }
    return render(request, "board/book_list.html", context)


def book_add(request):
    form = BooksForm()
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            book = form.save(False)
            book.author = request.user
            book.created = timezone.now()
            book.updated = timezone.now()
            book.save()
            return redirect('board:book-list')

    context = {
        "form": form
    }
    return render(request, "board/book_add.html", context)


def book_detail(request, book_id):

    book = Books.objects.get(id=book_id)
    bookcontents = BookContents.objects.filter(books=book_id)
    context = {
        "book": book,
        "bookcontents": bookcontents
    }
    return render(request, "board/book_detail.html", context)


def book_edit(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == "POST":
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.updated = timezone.now()
            book.save()
            return redirect('board:book-detail', book_id=book.id)
    else:
        form = BooksForm(instance=book)
    context = {
        "form": form,
        "book_id": book_id
    }
    return render(request, "board/book_edit.html", context)


def book_delete(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == "POST":
        form = BooksForm(request.POST, instance=book)
        print("Post.. ")
        if form.is_valid():
            book = form.save(commit=False)
            book.updated = timezone.now()
            book.is_deleted = True
            book.save()
            print("Valid..True ")
            return redirect('board:book-list')
        else:
            print("Valid..False ")
    else:
        form = BooksForm(instance=book)
    context = {
        "form": form,
        "book_id": book_id
    }
    return render(request, "board/book_delete.html", context)


def book_contents_add(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    form = BookContentsForm()
    print(book.id)
    if request.method == "POST":
        form = BookContentsForm(request.POST)
        print(request.POST.get('order_name'))
        if form.is_valid():
            contents = form.save(False)
            contents.books = book
            contents.save()
            return redirect('board:book-detail', book_id=book.id)
        else:
            print("not Valid")

    context = {
        "form": form,
        "book": book
    }
    return render(request, "board/book_detail.html", context)
