from django.contrib import admin
from .models import *

model=[Customer,Product,Bill,Order,Producttype]

# Register your models here.
admin.site.register(model)