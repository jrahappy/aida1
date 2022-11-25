from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Board
from .forms import BoardForm
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
