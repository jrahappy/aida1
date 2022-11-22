from django.urls import path
from .views import Board_list, Board_retrieve, Board_update, Board_delete, Board_create

app_name = 'board'
urlpatterns = [
    path('', Board_list, name='list'),
    path('post/<pk>/', Board_retrieve, name='detail'),
    path('post/<pk>/edit/', Board_update, name='update'),
    path('post/<pk>/delete/', Board_delete, name='delete'),
    path('add-post/', Board_create, name='create'),
]
