from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Customer

# Create your views here.


class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"


class CustomerListSearchView(CustomerListView):
    # Aufbereitung der daten um nur die passende bedingung zu rendern
    def get_queryset(self):
        # name ist der mitgegebene parameter in der url
        name = self.kwargs.get("name")
        # returned nur die values auf die die bedingung zutrifft und agiert von da an weiter wie die customer list view da diese extended wird
        return Customer.objects.filter(first_name__icontains=name)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'sales/detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj
