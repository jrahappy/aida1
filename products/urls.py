from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.product_create, name='create'),
    path('<pk>/', views.product_retrieve, name='detail'),
    # path('<pk>/edit/', views.product_update, name='update'),
    # path('<pk>/delete/', views.product_delete, name='delete'),

]
