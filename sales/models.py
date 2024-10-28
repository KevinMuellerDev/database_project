from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=30, help_text="Max. length of 30 chars")
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=False)
    email_address = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price} \n"


class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Total Amount: {self.total_amount}, Is Paid: {self.is_paid} \n"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Customer: {self.customer}, Products: {self.products}, Bill: {self.bill} \n"


class Producttype(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=300)

    def __str__(self):
        return f"Order: {self.order}, Product: {self.product}, Type Name: {self.type_name} \n"
