from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Board
from .forms import BoardForm


def Board_list(request):
    Boards = Board.objects.all()
    context = {
        "Boards": Boards
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
            return redirect('/')

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
            return render(request, 'board:detail', Post)

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
