from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.product_create, name='create'),
    path('<pk>/', views.product_retrieve, name='detail'),
    path('<pk>/edit/', views.product_update, name='update'),
    path('<pk>/editx/', views.product_edit_x, name='edit-x'),
    path('<pk>/editu/', views.product_edit_u, name='edit-u'),
    path('<pk>/editu/', views.product_edit_s, name='edit-s'),
    path('<pk>/delete/', views.product_delete, name='delete'),
    path('<pk>/delete_confirm/', views.product_delete_confirm, name='delete-confirm'),

]
