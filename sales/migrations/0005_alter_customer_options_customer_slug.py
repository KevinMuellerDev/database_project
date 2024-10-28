# Generated by Django 5.1.2 on 2024-10-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_bill_product_order_producttype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]