from django.urls import path
from django.views.generic import TemplateView
from .views import CustomerListView, CustomerCreate, CustomerDetail, CustomerModify, PersonCreate, add_person, person_list, edit_person, delete_confirm_person
# from . import views

app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('create/', CustomerCreate, name='create'),
    path('<uuid:id>/', CustomerDetail, name='detail'),
    path('<uuid:id>/modify/', CustomerModify, name='modify'),
    path('<uuid:id>/add/', PersonCreate, name='person_create'),
    # path('test/', views.TestView, name='test_view'),
    path('<uuid:id>/addperson/', add_person, name='add_person'),
    path('<uuid:id>/personlist/', person_list, name='person_list'),
    path('person/deleteconfirm/<int:person_id>/',
         delete_confirm_person, name='delete_confirm_person'),
    path('person/edit/<int:person_id>/', edit_person, name='edit_person'),
]
