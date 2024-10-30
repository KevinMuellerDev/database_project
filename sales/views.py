from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer

# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    
class CustomerListSearchView(CustomerListView):
    #aufbereitung der daten um nur die passende bedingung zu rendern
    def get_queryset(self):
       #name ist der mitgegebene parameter in der url 
        name=self.kwargs.get("name")
        # returned nur die values auf die die bedingung zutrifft und agiert von da an weiter wie die customer list view da diese extended wird
        return Customer.objects.filter(first_name__icontains=name)  