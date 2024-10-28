from django.contrib import admin
from .models import *

model=[Product,Bill,Order,Producttype]

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_filter=["first_name", "last_name"]
    

admin.site.register(Customer,AdminCustomer)
admin.site.register(model)