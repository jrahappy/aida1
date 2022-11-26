from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.Board_list, name='list'),
    path('post/<pk>/', views.Board_retrieve, name='detail'),
    path('post/<pk>/edit/', views.Board_update, name='update'),
    path('post/<pk>/delete/', views.Board_delete, name='delete'),
    path('add-post/', views.Board_create, name='create'),
    path('books/', views.book_list, name='book-list'),
    path('books/add/', views.book_add, name='book-add'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/edit/<int:book_id>/', views.book_edit, name='book-edit'),
    path('books/delete/<int:book_id>/', views.book_delete, name='book-delete'),
    path('books/contents/add/<int:book_id>',
         views.book_contents_add, name='book-contents-add'),

    # path('books/contents/edit/<int:book_contents_id>', book_contents_edit, name='book-contents_edit'),
    # path('books/contents/delete/<int:book__contents_id>', book_contents_delete, name='book-contents_delete'),


]
