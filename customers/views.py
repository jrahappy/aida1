import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views import View
from django.utils import timezone
from django.http import HttpResponseNotAllowed, HttpResponse

from .models import Customer, Person
from .forms import CustomerForm, PersonForm


def TestView(request):
    return render(request, 'customers/test.html')


class CustomerListView(ListView):

    context_object_name = 'customer_list'
    queryset = Customer.objects.all()
    template_name = 'customers/list.html'


def CustomerDetail(request, id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer
    }

    return render(request, 'customers/detail.html', context)


def CustomerModify(request, id):
    customer = get_object_or_404(Customer, pk=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated = timezone.now()
            customer.save()
            return redirect('customers:detail', id=customer.id)

    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form
    }

    return render(request, 'customers/modify.html', context)


def CustomerCreate(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():

            customer = form.save(commit=False)
            customer.author = request.user
            customer.created = timezone.now()
            customer.updated = timezone.now()
            customer.save()
            last_id = Customer.objects.last().id
            return redirect('customers:detail', last_id)

    context = {
        "form": form
    }
    return render(request, "customers/create.html", context)


def PersonCreate(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():

            person = form.save(commit=False)
            person.customer = customer
            person.created = timezone.now()
            person.updated = timezone.now()
            person.save()
            # last_id = Person.objects.last().id
            # print(last_id)
            return redirect('customers:detail', id=id)
    else:
        return HttpResponseNotAllowed('Only POST is allowed.')
    context = {
        'customer': customer,
        'form': form,
    }
    return render(request, "customers/detail.html", context)


def add_person(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.customer = customer
            person.created = timezone.now()
            person.updated = timezone.now()
            person.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "personListChanged": None,
                        "showMessage": f"{person.full_name} added."
                    })
                })
    else:
        form = PersonForm()
    context = {
        'customer': customer,
        'form': form,
    }
    return render(request, 'customers/_add_person.html', context)


def person_list(request, id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/_person_list.html', context)


def edit_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    customer = get_object_or_404(Customer, id=person.customer.id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.customer = customer
            person.updated = timezone.now()
            person.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "personListChanged": None,
                        "showMessage": f"{person.full_name} modified."
                    })
                })
    else:
        form = PersonForm(instance=person)
    context = {
        # 'customer': customer,
        'form': form,
    }
    return render(request, 'customers/_edit_person.html', context)


def delete_confirm_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        person.deleted = timezone.now()
        person.is_deleted = True
        person.save()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "personListChanged": None,
                    "showMessage": f"this person is removed."
                })
            })
    else:
        form = PersonForm(instance=person)
    context = {
        'form': form,
    }
    return render(request, 'customers/_delete_confirm_person.html', context)
