from django.contrib import admin
from .models import *

model = [Product, Bill, Order, Producttype]

# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name","last_name","account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo"],
            },
        ),
    ]


admin.site.register(Customer, AdminCustomer)
admin.site.register(model)
