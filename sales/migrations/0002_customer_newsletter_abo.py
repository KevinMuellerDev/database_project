# Generated by Django 5.1.2 on 2024-10-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='newsletter_abo',
            field=models.BooleanField(default=False),
        ),
    ]
